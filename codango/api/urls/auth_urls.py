from django.conf.urls import url, include
from api.views import auth_views



urlpatterns = [
    url(r'^users/$', auth_views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', auth_views.UserDetail.as_view()),
    url(r'^register/$', auth_views.UserRegister.as_view(), name='register'),
    url(r'^logout/$', auth_views.UserLogOut.as_view(), name='logout'),
    url(r'^recover/$', auth_views.UserRecover.as_view(), name='recover'),
    url(r'^reset/$', auth_views.UserReset.as_view(), name='reset')
]

urlpatterns += [
    url(r'^login/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^verify/', 'rest_framework_jwt.views.verify_jwt_token'),
]