from django.conf.urls import url
from api.views import resources_views, comments_views, votes_views, userprofile_views, pairprogram_views

urlpatterns = [
    url(r'^resources/$', resources_views.resources_list),
    url(r'^comments/$', comments_views.comments_list),
    url(r'^pairprogram/sessions/$', pairprogram_views.sessions_list),
    url(r'^pairprogram/participants/$', pairprogram_views.participants_list),
    url(r'^userprofile/$', userprofile_views.userprofile_list),
    url(r'^userprofile/follows/$', userprofile_views.follow_list),
    url(r'^userprofile/languages/$', userprofile_views.language_list),
    url(r'^userprofile/notifications/$', userprofile_views.notification_list),
    url(r'^votes/$', votes_views.votes_list),
]
