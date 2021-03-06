import psycopg2

from rest_framework import generics, permissions
# from serializers import UserSerializer, UserFollowSerializer, UserSettingsSerializer
from serializers import UserSerializer, UserFollowSerializer, UserSettingsSerializer
from serializers import AllUsersSerializer, UserRegisterSerializer
from userprofile import serializers, models
from django.contrib.auth.models import User
from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Custom of class IsOwnerOrReadOnly(permissions.BasePermission)
    That an APIexception is raised instead
    We do not want a ReadOnly
    """

    def has_object_permission(self, request, view, obj):

        # First check if authentication is True
        permission_classes = (permissions.IsAuthenticated, )
        # Instance is the user
        return obj.id == request.user.id


class UserListAPIView(generics.ListAPIView):
    """For /api/v1/users/ url path"""

    queryset = User.objects.all()
    serializer_class = AllUsersSerializer
    permission_classes = (permissions.IsAdminUser,)


class UserDetailAPIView(generics.RetrieveUpdateAPIView):
    """For /api/v1/users/<id> url path"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwner, )


class UserRegisterAPIView(generics.CreateAPIView):
    """For /api/v1/auth/register url path"""
    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


class UserLogoutAPIView(generics.UpdateAPIView):
    """For /api/v1/auth/logout url path"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwner, )


class UserFollowAPIView(generics.CreateAPIView):
    """
    For api/v1/users/<>/follow/ url path
    To enable user to add or remove those that they follow
    """

    serializer_class = UserFollowSerializer

    def get_queryset(self):
        to_be_followed = User.objects.filter(id=self.kwargs['pk']).first()
        return to_be_followed

    def perform_create(self, serializer):
        self.user = User.objects.filter(id=self.request.user.id).first()
        try:
            models.Follow.objects.create(
                follower=self.user, followed=self.get_queryset())
            return {"message":
                    "You have followed user'{}'".format(
                        self.get_queryset())}, 201
        except:
            raise serializers.serializers.ValidationError(
                'You have already followed this person')



class UserSettingsAPIView(generics.RetrieveUpdateAPIView):
    """
    For api/v1/users/<>/settings/ url path
    To enable user to update those that their:
    - update's frequency, github account and image
    """
    """For api/v1/users/<>/settings/ url path"""

    queryset = models.UserSettings.objects.all()
    serializer_class = UserSettingsSerializer
    permission_classes = (IsOwner,)
