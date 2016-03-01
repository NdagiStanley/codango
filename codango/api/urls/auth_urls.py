from django.conf.urls import url
from api.views import auth_views



urlpatterns = [
    url(r'^users/$', auth_views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', auth_views.UserDetail.as_view()),
    # url(r'^register/$', views.UserViewSet.as_view(), name='register'),
    # url(r'^login/$', views.UserViewSet.as_view(), name='login'),
    # url(r'^logout/$', views.UserViewSet.as_view(), name='logout'),
    # url(r'^recover/$', views.UserViewSet.as_view(), name='recover'),
    # url(r'^reset/$', views.UserViewSet.as_view(), name='reset')


]
