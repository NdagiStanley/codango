from django.contrib.auth.models import User

from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token


from api import serializers

# Default permission_classes = (permissions.IsAuthenticated,)


# This class is here for purposes of my own understanding
class UserList(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


# This class is here for purposes of my own understanding
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserRegister(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserReset(generics.UpdateAPIView):
    # Accept token to eneble set_password()

    # queryset should be password
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserRecover(generics.UpdateAPIView):
    permission_classes = (permissions.AllowAny,)

    # queryset should be password
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserLogOut(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
