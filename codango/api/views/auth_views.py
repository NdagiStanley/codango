from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.authtoken.models import Token


from api import serializers


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer