from datetime import datetime, timedelta

import jwt
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from config import settings


class UsersManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('email kiriting')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        return user

    def create_superuser(self, email, password=None):
        if not password:
            raise ValueError('password kiriting')
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_admin = True
        user.save()
        return user


class Users(AbstractBaseUser):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UsersManager()

    def __str__(self):
        return self.email

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True
