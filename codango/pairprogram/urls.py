from django.conf import settings
from django.conf.urls import url
from pairprogram import views
urlpatterns = [
    url(r'^$',
        views.ListSessionView.as_view(), name='list_sessions'),
    url(r'^(?P<session_id>[0-9]+)$',
        views.PairSessionView.as_view(), name='pair_program'),
    url(r'^start/$',
        views.StartPairView.as_view(), name='start_session'),
]