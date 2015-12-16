from django.conf import settings
from django.conf.urls import url
from pairprogram import views


urlpatterns = [

    url(r'^$',
        views.PairView.as_view(), name='view_pair_session'),
    url(r'^(?P<session_id>[0-9]+)$',
        views.PairSessionView.as_view(), name='pair_program'),
    url(r'^start/$',
        views.StartPairView.as_view(), name='pair_program'),

]