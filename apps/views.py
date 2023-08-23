from django.shortcuts import render
from .models import User
from .serializers import UserSerializers
from rest_framework import generics


class UserGetView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
