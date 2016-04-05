from rest_framework import serializers

from django.contrib.auth.models import User
from userprofile.models import UserProfile
from userprofile.serializers import UserProfileSerializer, NotificationSerializer
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

        read_only_fields = ('userprofile')


class UserSettingsSerializer(serializers.ModelSerializer):
    """User settings serializer"""

    userprofile = UserProfileSerializer(required=False)

    class Meta:
        model = User

        # Note that id is non-updatable, therefore not required in the read-only fields
        fields = ('username', 'email', 'password', 'userprofile',)

    def update(self, instance, validated_data):
        #
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.set_password(validated_data.get('password'))
        instance.userprofile.first_name = validated_data['userprofile'].get('first_name')
        instance.userprofile.last_name = validated_data['userprofile'].get('last_name')
        instance.userprofile.place_of_work = validated_data['userprofile'].get('place_of_work')
        instance.userprofile.position = validated_data['userprofile'].get('position')
        instance.userprofile.about = validated_data['userprofile'].get('about')
        instance.userprofile.github_username = validated_data['userprofile'].get('github_username')
        instance.userprofile.frequency = validated_data['userprofile'].get('frequency')
        instance.save()
        instance.userprofile.save()
        return instance


class UserFollowSerializer(serializers.ModelSerializer):
    """UserSettings Serializer to be used in /api/v1/users/<>/follow/"""

    class Meta:
        model = User

        # Note that id is non-updatable, therefore not required in the read-only fields
        fields = ('id', 'following')
