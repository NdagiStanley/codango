from django.conf.urls import url, include
from rest_framework import routers

from api import views
import api.urls.auth_urls


urlpatterns = [
    # Including the api/v1/auth/... routes
    url(r'^auth/', include(api.urls.auth_urls)),

    # The other routes included in the api/v1 route
    url(r'^resources/$', views.ResourceViewSet.as_view(), \
        name='resources-list'),
    url(r'^userprofile/$', views.UserProfileViewSet.as_view(), \
        name='userprofile-list'),
    url(r'^userprofile/follows/$', views.FollowViewSet.as_view(), \
        name='follow-list'),
    url(r'^userprofile/languages/$', views.LanguageViewSet.as_view(), \
        name='language-list'),
    url(r'^userprofile/notifications/$', views.NotificationViewSet.as_view(), \
        name='notification-list'),
    url(r'^comments/$', views.CommentViewSet.as_view(), name='comments-list'),
    url(r'^pairprogram/sessions/$', views.SessionViewSet.as_view(), \
        name='sessions-list'),
    url(r'^pairprogram/participants/$', views.ParticipantViewSet.as_view(), \
        name='participants-list'),
    url(r'^votes/$', views.VoteViewSet.as_view(), name='votes-list')
]
