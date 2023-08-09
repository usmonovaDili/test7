# Generated by Django 4.2.4 on 2023-08-09 17:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('date_join', models.DateTimeField(auto_now_add=True, verbose_name='data joined')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(choices=[(False, 'Teacher'), (True, 'student')], default=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.DateField(default=datetime.date(2023, 8, 9))),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
