from django.shortcuts import render
from .models import Users
from .serializers import RegistrationSerializer,LoginSerializer,UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class ListCreateUserView(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class RetrieveUpdateDestroyUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]
