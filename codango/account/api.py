from rest_framework import generics, permissions
from serializers import UserSerializer
from django.contrib.auth.models import User


class UserList(generics.ListAPIView):
    """For /api/v1/users/ url path"""
    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()
    serializer_class = UserSerializer

class SpecificUserList(generics.RetrieveUpdateAPIView):
    """For /api/v1/users/<id> url path"""
    permission_classes = (permissions.AllowAny,)

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
