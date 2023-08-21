from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import Users


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = Users
        fields = ['email', 'username', 'password', 'token']

    def create(self, validated_data):
        return Users.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):

        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'email kiriting'
            )

        if password is None:
            raise serializers.ValidationError(
                'parol kiriting'
            )

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'foydalanuvchi topilmadi'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'faydalanuvchi uchirilgan'
            )

        return {
            'email': user.email,
            'username': user.username,
            'token': user.token
        }


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100, min_length=8, write_only=True)

    class Meta:
        model = Users
        fields = '__all__'

        read_only_fields = ('tokens', 'is_staff')

        def update(self, instance, validated_data):

            password = validated_data.pop('password', None)

            for (key, value) in validated_data.items():
                setattr(instance, key, value)

            if password is not None:
                instance.set_password(password)

            instance.save()

            return instance
