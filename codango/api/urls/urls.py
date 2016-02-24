from django.conf.urls import url, include
from rest_framework import routers

from api.views import *
import api.urls.auth_urls

router = routers.DefaultRouter()
router.register(r'^register', UserViewSet, 'registers')

urlpatterns = [
    # Including the api/v1/auth/... routes
    url(r'^auth/', include(api.urls.auth_urls)),

    # The other routes included in the api/v1 route
    url(r'^', include(router.urls)),
    url(r'^resources/$', ResourceViewSet.as_view(), name='resources-list'),
    url(r'^userprofile/$', UserProfileViewSet.as_view(
        {'get': 'list'}), name='userprofile-list'),
    url(r'^userprofile/follows/$', FollowViewSet.as_view(
        {'get': 'list'}), name='follow-list'),
    url(r'^userprofile/languages/$', LanguageViewSet.as_view(
        {'get': 'list'}), name='language-list'),
    url(r'^userprofile/notifications/$', NotificationViewSet.as_view(
        {'get': 'list'}), name='notification-list'),
    url(r'^comments/$', CommentViewSet.as_view(
        {'get': 'list'}), name='comments-list'),
    url(r'^pairprogram/sessions/$', SessionViewSet.as_view(
        {'get': 'list'}), name='sessions-list'),
    url(r'^pairprogram/participants/$', ParticipantViewSet.as_view(
        {'get': 'list'}), name='participants-list'),
    url(r'^votes/$', VoteViewSet.as_view(
        {'get': 'list'}), name='votes-list')
]
