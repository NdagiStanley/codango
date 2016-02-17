from rest_framework import serializers
from userprofile.models import UserProfile, Follow, Language, Notification

class UserProfileSerializer(serializers.ModelSerializer):
    """
    UserProfile Serializer
    """
    class Meta:
        model = UserProfile
        fields = ('user', 'social_id', 'first_name', 'last_name', 'place_of_work', 'position', 'about', 'github_username', 'frequency', 'image')

class FollowSerializer(serializers.ModelSerializer):
    """
    Follow Serializer
    """
    class Meta:
        model = Follow
        fields = ('follower', 'followed', 'date_of_follow')

class LanguageSerializer(serializers.ModelSerializer):
    """
    Language Serializer
    """
    class Meta:
        model = Language
        fields = ('user', 'name')

class NotificationSerializer(serializers.ModelSerializer):
    """
    Notification Serializer
    """
    class Meta:
        model = Notification
        fields = ('user', 'link', 'activity_type', 'read', 'content', 'date_created')
