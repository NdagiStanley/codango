from rest_framework import serializers

from models import UserProfile, Follow, Notification, Language


class FollowSerializer(serializers.ModelSerializer):
    """Follow Serializer"""

    class Meta:
        model = Follow
        fields = ('follower', 'followed', 'date_of_follow')

        read_only_fields = ('date_of_follow', 'follower')


class UserProfileSerializer(serializers.ModelSerializer):
    """UserProfile Serializer"""

    # follows = FollowSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'place_of_work', 'position', 'about', 'github_username', 'frequency', 'followers', 'followings')


class UserSettingsSerializer(serializers.ModelSerializer):
    """UserSettings Serializer"""

    class Meta:
        model = UserProfile
        fields = ('frequency', 'github_username', 'id')


class LanguageSerializer(serializers.ModelSerializer):
    """Language Serializer"""

    class Meta:
        model = Language
        fields = ('name',)


class NotificationSerializer(serializers.ModelSerializer):
    """Notification Serializer"""

    class Meta:
        model = Notification
        fields = ('link', 'activity_type', 'read',
                  'content', 'date_created')

        read_only_fields = ('date_created', 'link', 'activity_type', 'content')
