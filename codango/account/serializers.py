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

    userprofile = UserProfileSerializer(required=False)

    class Meta:
        model = User

        # Note that id is non-updatable, therefore not required in the read-only fields
        fields = ('username', 'email', 'userprofile',)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_ = validated_data.get('last_name', instance.last_name)
        instance.last_ = validated_data.get('place_of_work', instance.userprofile.place_of_work)
        instance.last_ = validated_data.get('position', instance.userprofile.position)
        instance.last_ = validated_data.get('github_username', instance.userprofile.github_username)
        instance.last_ = validated_data.get('frequency', instance.userprofile.frequency)
        return instance



class UserFollowSerializer(serializers.ModelSerializer):
    """UserSettings Serializer to be used in /api/v1/users/<>/follow/"""

    # follow = FollowSerializer()

    class Meta:
        model = User

        # Note that id is non-updatable, therefore not required in the read-only fields
        fields = ('id', 'follower')
