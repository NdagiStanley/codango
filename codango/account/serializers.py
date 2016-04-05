from rest_framework import serializers

from django.contrib.auth.models import User
from userprofile.models import UserProfile, UserSettings
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
        UserSettings.objects.create(user_id=user.id)
        return user


class UserSerializer(serializers.ModelSerializer):
    """User serializer"""

    # confirm_password = serializers.CharField(max_length=32, required=True)
    userprofile = UserProfileSerializer(required=False)

    class Meta:
        model = User

        # Note that id is non-updatable, therefore not required in the read-only fields
        fields = ('username', 'email', 'password', 'userprofile')

        write_only_fields = ('password')
        # read_only_fields = ('confirm_password')

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.userprofile.first_name = validated_data['userprofile'].get('first_name', instance.userprofile.first_name)
        instance.userprofile.last_name = validated_data['userprofile'].get('last_name', instance.userprofile.last_name)
        instance.userprofile.place_of_work = validated_data['userprofile'].get('place_of_work', instance.userprofile.place_of_work)
        instance.userprofile.position = validated_data['userprofile'].get('position', instance.userprofile.position)
        instance.userprofile.github_username = validated_data['userprofile'].get('github_username', instance.userprofile.github_username)
        instance.userprofile.about = validated_data['userprofile'].get('about', instance.userprofile.about)
        instance.save()
        if not validated_data.get('password'):
            instance.password = instance.password
            instance.save()
            return instance
        # instance.save()
        # password = validated_data.get('password', None)
        # confirm_password = validated_data.get('confirm_password', None)
        # if password and confirm_password and password == confirm_password:
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance



class UserSettingsSerializer(serializers.ModelSerializer):
    """User settings serializer"""

    class Meta:
        model = UserSettings

        # Note that id is non-updatable, therefore not required in the read-only fields
        fields = ('languages', 'frequency')

        read_only_fields = ('languages')


class UserFollowSerializer(serializers.ModelSerializer):
    """UserSettings Serializer to be used in /api/v1/users/<>/follow/"""

    class Meta:
        model = User

        # Note that id is non-updatable, therefore not required in the read-only fields
        fields = ('id', 'following')
