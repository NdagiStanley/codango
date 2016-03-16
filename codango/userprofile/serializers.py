from rest_framework import serializers

from models import UserProfile, Follow, Notification, Language


class UserProfileSerializer(serializers.ModelSerializer):
    """UserProfile Serializer"""

    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name',
                  'place_of_work', 'position', 'about', 'github_username',
                  'frequency', 'image')


class FollowSerializer(serializers.ModelSerializer):
    """Follow Serializer"""

    class Meta:
        model = Follow
        fields = ('follower', 'followed', 'date_of_follow')

        read_only_fields = ('date_of_follow')


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
