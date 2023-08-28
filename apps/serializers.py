from rest_framework import serializers, exceptions
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import TokenError, RefreshToken

from .models import User
from .utils import validate_email as email_validate


class UserAllSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer[User]):
    password = serializers.CharField(max_length=120, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'password',
            'bio',
            'name',
        ]

    def validate_email(self, value: str):
        valid, error_text = email_validate(value)
        if not valid:
            raise serializers.ValidationError(error_text)
        try:
            email_name, domain_part = value.strip().rsplit('@', 1)
        except ValueError:
            pass
        else:
            value = '@'.join([email_name, domain_part.lower()])
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'], password=validated_data['password']
        )
        user.bio = validated_data.get('bio', '')
        user.name = validated_data.get('name', '')
        user.save(update_fields=['bio', 'name'])
        return user


class LoginSerializers(serializers.ModelSerializer[User]):
    email = serializers.CharField(max_length=200)
    username = serializers.CharField(max_length=200, read_only=True)
    password = serializers.CharField(max_length=200, write_only=True)
    is_staff = serializers.BooleanField(read_only=True)

    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = User.objects.get(email=obj.email)

        return {'refresh': user.tokens['refresh'], 'access': user.tokens['access']}

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'tokens', 'is_staff']

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError('tizimga kirish uchun email kiriting')

        if password is None:
            raise serializers.ValidationError('parol kiriting')

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError('foydalanuvchi email yoki paroli topilmadi')
        if not user.is_active:
            raise serializers.ValidationError('foydalanuvchi faol emas')

        return user


class UserSerializers(serializers.ModelSerializer[User]):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'password',
            'tokens',
            'bio',
            'full_name',
            'birth_date',
            'is_staff',
        )
        read_only_fields = ('tokens', 'is_staff')

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.ser_password(password)
        instance.save()
        return instance


class LogoutSerializers(serializers.Serializer[User]):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs['refresh']

        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            raise exceptions.AuthenticationFailed(TokenError)
