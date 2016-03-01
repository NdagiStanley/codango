# Imports to enable APIView
from rest_framework.views import APIView
from rest_framework.response import Response

# Import models
from resources.models import Resource
from userprofile.models import UserProfile, Follow, Language, Notification
from votes.models import Vote
from comments.models import Comment
from pairprogram.models import Session, Participant

# Import serializers
from api import serializers


class ResourceViewSet(APIView):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    def get(self, request):
        resources = Resource.objects.all()
        serializer = serializers.ResourceSerializer(resources, many=True)
        return Response(serializer.data)


class UserProfileViewSet(APIView):
    def get(self, request):
        userprofiles = UserProfile.objects.all()
        serializer = serializers.UserProfileSerializer(userprofiles, many=True)
        return Response(serializer.data)


class FollowViewSet(APIView):
    def get(self, request):
        follows = Follow.objects.all()
        serializer = serializers.FollowSerializer(follows, many=True)
        return Response(serializer.data)


class LanguageViewSet(APIView):
    def get(self, request):
        languages = Language.objects.all()
        serializer = serializers.LanguageSerializer(languages, many=True)
        return Response(serializer.data)


class NotificationViewSet(APIView):
    def get(self, request):
        notifications = Notification.objects.all()
        serializer = serializers.NotificationSerializer(notifications,
                                                        many=True)
        return Response(serializer.data)


class VoteViewSet(APIView):
    def get(self, request):
        votes = Vote.objects.all()
        serializer = serializers.VoteSerializer(votes, many=True)
        return Response(serializer.data)


class CommentViewSet(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = serializers.CommentSerializer(comments, many=True)
        return Response(serializer.data)


class SessionViewSet(APIView):
    def get(self, request):
        sessions = Session.objects.all()
        serializer = serializers.SessionSerializer(sessions, many=True)
        return Response(serializer.data)


class ParticipantViewSet(APIView):
    def get(self, request):
        participants = Participant.objects.all()
        serializer = serializers.ParticipantSerializer(participants, many=True)
        return Response(serializer.data)
