from rest_framework import serializers

from django.contrib.auth.models import User
from userprofile.serializers import UserProfileSerializer, NotificationSerializer
from userprofile.serializers import LanguageSerializer



class UserSerializer(serializers.ModelSerializer):
    """User serializer"""
    class Meta:
        model = User

        # Note that id is non-updatable, therefore not required in the read-only fields
        fields = ('id', 'username', 'email')

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserSettingsSerializer(serializers.ModelSerializer):
    """UserSettings Serializer to be used in /api/v1/users/<>/settings/"""

    userprofile = UserProfileSerializer()
    languages = LanguageSerializer()
    notifications = NotificationSerializer()

    class Meta:
        model = User

        # Note that id is non-updatable, therefore not required in the read-only fields
        fields = ('id', 'username', 'email', 'password', 'userprofile', 'languages', 'notifications')
