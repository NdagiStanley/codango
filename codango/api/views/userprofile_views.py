from rest_framework import viewsets

from userprofile.models import UserProfile, Follow, Language, Notification
from api.serializers.userprofile_serializers import UserProfileSerializer, FollowSerializer, NotificationSerializer, LanguageSerializer


class UserProfileViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class FollowViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer


class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
