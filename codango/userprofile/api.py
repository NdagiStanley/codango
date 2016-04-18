from rest_framework import generics

from serializers import UserProfileSerializer, FollowSerializer, NotificationSerializer, LanguageSerializer
from models import UserProfile, Follow, Notification, Language


class UserProfileListAPIView(generics.ListCreateAPIView):
    """For /api/v1/userprofiles/ url path"""
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """For /api/v1/userprofile/<> url path"""
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class FollowListAPIView(generics.ListCreateAPIView):
    """For /api/v1/userprofile/follows/ url path"""
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer


class FollowDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """For /api/v1/userprofile/follows/<> url path"""
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer


class LanguageListAPIView(generics.ListCreateAPIView):
    """For /api/v1/userprofile/langauges/ url path"""
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class LanguageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """For /api/v1/userprofile/langauges/<> url path"""
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class NotificationListAPIView(generics.ListCreateAPIView):
    """For /api/v1/userprofile/notifications/ url path"""
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class NotificationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """For /api/v1/userprofile/notifications/<> url path"""
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
