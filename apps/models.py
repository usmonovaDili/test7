import datetime

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin

# Create your models here.

from django.db import models


class CustomUser(BaseUserManager):
    def create_user(self, email, username, name, age, password=None, **extra_fields):
        if not email:
            raise ValueError('email kiritilish shart!')
        if not username:
            raise ValueError('"username" kiritilmadi ')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            name=name,
            age=age,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, name, age, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            name=name,
            age=age,
            password=password
        )


class User(AbstractBaseUser):
    STAFF_CHOICES = (
        (False, 'Teacher'),
        (True, 'student'),
    )
    email = models.EmailField(verbose_name='email', max_length=50, unique=True)
    username = models.CharField(max_length=50, unique=True)
    date_join = models.DateTimeField(verbose_name='data joined', auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(choices=STAFF_CHOICES, default=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.DateField(default=datetime.date.today())

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'age']

    objects = CustomUser()

    def __str__(self):
        return f'{self.username} {self.email}'

    def has_perm(self, perm, obj=None):
        return self.is_admin
