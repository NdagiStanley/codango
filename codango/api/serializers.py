from django.contrib.auth.models import User

from rest_framework import serializers
from resources.models import Resource
from userprofile.models import UserProfile, Follow, Language, Notification
from votes.models import Vote
from comments.models import Comment
from pairprogram.models import Session, Participant


class ResourceSerializer(serializers.ModelSerializer):
    """Resource Serializer"""
    class Meta:
        model = Resource
        fields = ('author', 'text', 'language_tags', 'resource_file', 'resource_file_name', 'resource_file_size', 'snippet_text', 'date_added', 'date_modified')

class UserProfileSerializer(serializers.ModelSerializer):
    """UserProfile Serializer"""
    class Meta:
        model = UserProfile
        fields = ('user', 'social_id', 'first_name', 'last_name', 'place_of_work', 'position', 'about', 'github_username', 'frequency', 'image')

class FollowSerializer(serializers.ModelSerializer):
    """Follow Serializer"""
    class Meta:
        model = Follow
        fields = ('follower', 'followed', 'date_of_follow')

class LanguageSerializer(serializers.ModelSerializer):
    """Language Serializer"""
    class Meta:
        model = Language
        fields = ('user', 'name')

class NotificationSerializer(serializers.ModelSerializer):
    """Notification Serializer"""
    class Meta:
        model = Notification
        fields = ('user', 'link', 'activity_type', 'read', 'content', 'date_created')

class VoteSerializer(serializers.ModelSerializer):
    """Vote Serializer"""
    class Meta:
        model = Vote
        fields = ('user', 'resource', 'vote', 'time_stamp')

class CommentSerializer(serializers.ModelSerializer):
    """Comment Serializer"""
    class Meta:
        model = Comment
        fields = ('author', 'resource', 'content', 'date_created', 'date_modified')

class SessionSerializer(serializers.ModelSerializer):
    """Session Serializer"""
    class Meta:
        model = Session
        fields = ('session_name', 'last_active_date', 'status', 'initiator')

class ParticipantSerializer(serializers.ModelSerializer):
    """Participant serializer"""
    class Meta:
        model = Participant
        fields = ('participant', 'session', 'joined_date')


class UserSerializer(serializers.ModelSerializer):
    """User serializer"""
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
