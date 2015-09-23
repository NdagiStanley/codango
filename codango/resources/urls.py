from django.conf.urls import url
from resources import views

urlpatterns = [
    url(r'^create', views.ResourceCreate.as_view(), name='resources_create'),

    url(r'^list', views.ResourceList.as_view(), name='resources_list'),

    url(r'^create', views.ResourceCreate.as_view(), name='resources_create'),

    url(r'^list', views.ResourceList.as_view(), name='resources_list'),

    url(r'^(?P<pk>[0-9]+)/$', views.ResourceDetail.as_view(), name='resources_detail'),

    url(r'^(?P<pk>[0-9]+)/$', views.ResourceDetail.as_view(),
        name='resources_detail'),

    url(r'^(?P<pk>[0-9]+)/update/$', views.ResourceUpdate.as_view(),
        name='resources_update'),
]
