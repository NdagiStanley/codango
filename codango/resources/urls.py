from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',
        views.ResourceList.as_view(),
        name='resource_list'),

    url(r'^(?P<pk>[0-9]+)/$',
        views.ResourceDetail.as_view(),
        name='resource_detail'),

    url(r'^create/$',
        views.ResourceCreate.as_view(),
        name='resource_create'),

    url(r'^(?P<pk>[0-9]+)/update/$',
        views.ResourceUpdate.as_view(),
        name='resource_edit'),
    
    url(r'^(?P<pk>[0-9]+)/delete/$',
        views.ResourceDelete.as_view(),
        name='resource_delete'),
]