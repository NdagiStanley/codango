from django.conf.urls import url
from api.views import resources_views, comments_views, votes_views, userprofile_views, pairprogram_views

from api.views.resources_views import ResourceViewSet
from api.views.comments_views import CommentViewSet
from api.views.votes_views import VoteViewSet
from api.views.pairprogram_views import SessionViewSet, ParticipantViewSet
from api.views.userprofile_views import UserProfileViewSet, FollowViewSet, LanguageViewSet, NotificationViewSet
from rest_framework import renderers

resources_list = ResourceViewSet.as_view({
    'get': 'list',
    # 'post': 'create'
})

comments_list = CommentViewSet.as_view({
    'get': 'list',
    # 'post': 'create'
})

votes_list = VoteViewSet.as_view({
    'get': 'list',
    # 'post': 'create'
})

sessions_list = SessionViewSet.as_view({
    'get': 'list',
    })

participants_list = ParticipantViewSet.as_view({
    'get': 'list',
    })

userprofile_list = UserProfileViewSet.as_view({
    'get': 'list',
    })

follow_list = FollowViewSet.as_view({
    'get': 'list',
    })

language_list = LanguageViewSet.as_view({
    'get': 'list',
    })

notification_list = NotificationViewSet.as_view({
    'get': 'list',
    })

urlpatterns = [
    url(r'^resources/$', resources_list, name = 'resources-list'),
    url(r'^comments/$', comments_list, name = 'comments-list'),
    url(r'^pairprogram/sessions/$', sessions_list, name = 'sessions-list'),
    url(r'^pairprogram/participants/$', participants_list, name = 'participants-list'),
    url(r'^userprofile/$', userprofile_list, name = 'userprofile-list'),
    url(r'^userprofile/follows/$', follow_list, name = 'follow-list'),
    url(r'^userprofile/languages/$', language_list, name = 'language-list'),
    url(r'^userprofile/notifications/$', notification_list, name = 'notification-list'),
    url(r'^votes/$', votes_list, name = 'votes-list'),
]
