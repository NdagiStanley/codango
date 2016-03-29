from rest_framework import serializers

from django.contrib.auth.models import User
from userprofile.models import UserProfile
from userprofile.serializers import UserProfileSerializer, NotificationSerializer, UserSettingsSerializer
from userprofile.serializers import FollowSerializer


class AllUsersSerializer(serializers.ModelSerializer):
    """User serializer"""

    class Meta:
        model = User

        # Note that id is non-updatable, therefore not required in the read-only fields
        fields = ('id', 'username',)


class UserRegisterSerializer(serializers.ModelSerializer):
    """User serializer"""

    class Meta:
        model = User

        # Note that id is non-updatable, therefore not required in the read-only fields
        fields = ('id', 'username', 'password', 'email',)

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    """User serializer"""

    userprofile = UserProfileSerializer(read_only=True)

    class Meta:
        model = User

        # Note that id is non-updatable, therefore not required in the read-only fields
        fields = ('username', 'email', 'userprofile',)

        read_only_fields = ('userprofile',)


class UserFollowSerializer(serializers.ModelSerializer):
    """UserSettings Serializer to be used in /api/v1/users/<>/follow/"""

    # follow = FollowSerializer()

    class Meta:
        model = User

        # Note that id is non-updatable, therefore not required in the read-only fields
        fields = ('id', 'follower')
