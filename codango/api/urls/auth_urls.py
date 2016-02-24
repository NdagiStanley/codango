from django.conf.urls import url
from api.views import *

urlpatterns = [
    url(r'^register/$', UserViewSet.as_view(
        {'get': 'list'}), name='register'),
    url(r'^login/$', UserViewSet.as_view(
        {'get': 'list'}), name='login'),
    url(r'^logout/$', UserViewSet.as_view(
        {'get': 'list'}), name='logout'),
    url(r'^recover/$', UserViewSet.as_view(
        {'get': 'list'}), name='recover'),
    url(r'^reset/$', UserViewSet.as_view(
        {'get': 'list'}), name='reset')
]
