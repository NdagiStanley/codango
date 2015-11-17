from django.conf import settings
from django.conf.urls import url
from userprofile import views


urlpatterns = [

    url(r'^(?P<username>\w+)$',
        views.UserProfileDetailView.as_view(), name='user_profile'),
    url(r'^(?P<username>\w+)/edit$',
        views.UserProfileEditView.as_view(), name='edit_user_profile'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
    url(r'^(?P<username>\w+)/follow$',
        views.FollowUserView.as_view(), name='follow_user'),
    url(r'^(?P<username>\w+)/followers',
        views.FollowersView.as_view(), name='followers'),
    url(r'^(?P<username>\w+)/following',
        views.FollowingView.as_view(), name='following'),
]