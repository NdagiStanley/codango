from django.conf.urls import url, include
from api.views import auth_views



urlpatterns = [
    url(r'^register/$', auth_views.UserRegister.as_view(), name='register'),
    url(r'^logout/$', auth_views.UserLogOut.as_view(), name='logout'),
]

urlpatterns += [
    url(r'^login/', 'rest_framework_jwt.views.obtain_jwt_token'),
]