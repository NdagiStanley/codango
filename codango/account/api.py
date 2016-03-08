from rest_framework import generics, permissions
from serializers import UserSerializer
from django.contrib.auth.models import User


class UserRegisterAPIView(generics.CreateAPIView):
    """For /api/v1/auth/register url path"""
    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserLogoutAPIView(generics.UpdateAPIView):
    """For /api/v1/auth/logout url path"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
