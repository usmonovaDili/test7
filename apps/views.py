from rest_framework import generics
from .models import User
from .serializers import UserSerializers


class CustomUserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class CustomUserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    lookup_url_kwarg = 'user_id'
