from django.contrib.auth.models import User
from rest_framework import viewsets

# imports to enable APIView
from rest_framework.views import APIView
from rest_framework.response import Response

from resources.models import Resource
from userprofile.models import UserProfile, Follow, Language, Notification
from votes.models import Vote
from comments.models import Comment
from pairprogram.models import Session, Participant
from api.serializers import *

class ResourceViewSet(APIView):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    def get(self, request):
        resources = Resource.objects.all()
        serializer = ResourceSerializer(resources, many=True)
        return Response(serializer.data)

# Without APIView
# class ResourceViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     This viewset automatically provides `list` and `detail` actions.
#     """
#     queryset = Resource.objects.all()
#     serializer_class = ResourceSerializer


class UserProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class FollowViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer


class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class VoteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


class CommentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class SessionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class ParticipantViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer


class UserViewSet(viewsets.ModelViewSet):
    """UserViewSet from the inbuilt User Model"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
