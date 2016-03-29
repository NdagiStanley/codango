from rest_framework import generics, permissions
from serializers import UserSerializer, UserFollowSerializer
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
        models.Follow.objects.create(follower=self.user, followed=self.get_queryset())
        # import ipdb; ipdb.set_trace()
        # return models.Follow.objects.filter(follower=self.user, followed=self.get_queryset())


class UserSettingsAPIView(generics.RetrieveUpdateAPIView):
    """
    For api/v1/users/<>/settings/ url path
    To enable user to update those that their:
    - username, password, update's frequency, github account and image
    """
    """For api/v1/users/<>/settings/ url path"""

    queryset = User.objects.all()
    serializer_class = serializers.UserSettingsSerializer
