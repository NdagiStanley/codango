from django.conf.urls import url
from userprofile import views


urlpatterns = [
    url(r'^auth/github$',views.UserGithub.as_view(), name='user_github'),
    url(r'^activity/$',views.ActivityUpdate.as_view(), name='user_activity'),
    url(r'^(?P<username>[_\w\.]+)$',
        views.UserProfileDetailView.as_view(), name='user_profile'),
    url(r'^(?P<username>[_\w\.]+)/edit$',
        views.UserProfileEditView.as_view(), name='edit_user_profile'),
    url(r'^(?P<username>[_\w\.]+)/follow$',
        views.FollowUserView.as_view(), name='follow_user'),
    url(r'^(?P<username>[_\w\.]+)/(?P<direction>following|followers)',
        views.FollowListView.as_view(), name='following'),
    url(r'^(?P<username>[_\w\.]+)/settings$',
        views.SettingsView.as_view(), name='settings'),
]
