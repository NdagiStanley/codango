from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^register/$', views.UserViewSet.as_view(), name='register'),
    url(r'^login/$', views.UserViewSet.as_view(), name='login'),
    url(r'^logout/$', views.UserViewSet.as_view(), name='logout'),
    url(r'^recover/$', views.UserViewSet.as_view(), name='recover'),
    url(r'^reset/$', views.UserViewSet.as_view(), name='reset')
]
