from django.conf.urls import url
from resources import views

urlpatterns = [
url(r'^/(?P<resource_id>[0-9]+)/(?P<action>\w+)$', views.VoteAjax.as_view(), name='vote'),
url(r'^/newresource$', views.AjaxCommunityView.as_view(), name='newresource'),
url(r'^ajax/community/(?P<community>\w+|)$',views.AjaxCommunityView.as_view(), name='community'),
]

