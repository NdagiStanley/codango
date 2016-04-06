from rest_framework import serializers

from django.contrib.auth.models import User
from userprofile.models import UserProfile, UserSettings
from userprofile.serializers import UserProfileSerializer, NotificationSerializer
from userprofile.serializers import FollowSerializer


class AllUsersSerializer(serializers.ModelSerializer):
    """Serializer for User model having only the field required for all users"""

    class Meta:
        model = User

        # Note that id is non-updatable, therefore not required in the read-only fields
        fields = ('id', 'username',)


class UserRegisterSerializer(serializers.ModelSerializer):
    """Serializer for User model having only the fields required for Registration"""

    # This field is not tied to any model. It is for server side authentication
    confirm_password = serializers.CharField(
        max_length=32, required=False, write_only=True)

    class Meta:
        model = User

        # Note that id is non-updatable, therefore not required in the read-only fields
        fields = ('id', 'username', 'password', 'confirm_password', 'email',)

    def create(self, validated_data):
        password = validated_data.get('password')
        confirm_password = validated_data.get('confirm_password')
        if password and confirm_password and password == confirm_password:
            user = User(
                email=validated_data['email'],
                username=validated_data['username'],
            )
            user.set_password(validated_data['password'])
            user.save()
            UserSettings.objects.create(user_id=user.id)
            return user
        raise serializers.ValidationError("Password and confirm_password don't tally")


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User Model having fields for user details"""

    username = serializers.CharField(max_length=100, required=False)
    email = serializers.EmailField(required=False)
    password = serializers.EmailField(required=False)

    # This field is not tied to any model. It is for server side authentication
    confirm_password = serializers.CharField(
        max_length=32, required=False, write_only=True)

    # Added the Serializer for UserProfile model for more details
    userprofile = UserProfileSerializer(required=False)

    class Meta:
        model = User

        # Note that id is non-updatable,
        # therefore not required in the read-only fields
        fields = ('username', 'email', 'password',
                  'confirm_password', 'userprofile')

        write_only_fields = ('password', 'email')

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.userprofile.first_name = validated_data.get(
            'userprofile', instance.userprofile.__dict__).get(
            'first_name', instance.userprofile.first_name)
        instance.userprofile.last_name = validated_data.get(
            'userprofile', instance.userprofile.__dict__).get(
            'last_name', instance.userprofile.last_name)
        instance.userprofile.place_of_work = validated_data.get(
            'userprofile', instance.userprofile.__dict__).get(
            'place_of_work', instance.userprofile.place_of_work)
        instance.userprofile.position = validated_data.get(
            'userprofile', instance.userprofile.__dict__).get(
            'position', instance.userprofile.position)
        instance.userprofile.github_username = validated_data.get(
            'userprofile', instance.userprofile.__dict__).get(
            'github_username', instance.userprofile.github_username)
        instance.userprofile.about = validated_data.get(
            'userprofile', instance.userprofile.__dict__).get(
            'about', instance.userprofile.about)
        instance.save()
        instance.userprofile.save()
        password = validated_data.get('password', None)
        confirm_password = validated_data.get('confirm_password', None)
        if password and confirm_password and password == confirm_password:
            instance.set_password(validated_data.get('password'))
            instance.save()
            return instance
        return instance


class UserSettingsSerializer(serializers.ModelSerializer):
    """User settings serializer"""

    class Meta:
        model = UserSettings

        # Note that id is non-updatable,
        # therefore not required in the read-only fields
        fields = ('languages', 'frequency')

        read_only_fields = ('languages')


class UserFollowSerializer(serializers.ModelSerializer):
    """UserSettings Serializer to be used in /api/v1/users/<>/follow/"""

    class Meta:
        model = User

        # Note that id is non-updatable,
        # therefore not required in the read-only fields
        fields = ('id', 'following')
