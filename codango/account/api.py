from rest_framework import generics, permissions
from serializers import UserSerializer, UserSettingsSerializer
from userprofile import serializers, models
from django.contrib.auth.models import User


class UserList(generics.ListAPIView):
    """For /api/v1/users/ url path"""

    queryset = User.objects.all()
    serializer_class = UserSerializer

class SpecificUserList(generics.RetrieveUpdateAPIView):
    """For /api/v1/users/<id> url path"""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRegisterAPIView(generics.CreateAPIView):
    """For /api/v1/auth/register url path"""
    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserLogoutAPIView(generics.UpdateAPIView):
    """For /api/v1/auth/logout url path"""

    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserFollowAPIView(generics.RetrieveUpdateAPIView):
    """
    For api/v1/users/<>/follow/ url path
    To enable user to add or remove those that they follow
    """

    queryset = models.Follow.objects.all()
    serializer_class = serializers.FollowSerializer

class UserSettingsAPIView(generics.RetrieveUpdateAPIView):
    """
    For api/v1/users/<>/settings/ url path
    To enable user to update those that their:
    - username, password, update's frequency, github account and image
    """
    """For api/v1/users/<>/settings/ url path"""

    queryset = User.objects.all()
    serializer_class = UserSettingsSerializer
