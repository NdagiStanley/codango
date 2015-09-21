from django.conf.urls import url
from account import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^home$', views.HomeView.as_view(), name='home'),
    url(r'^recovery/$', views.ForgotPassword.as_view(),
        name='forgot_password'),
    url(r'^recovery/(?P<user_hash>([a-z0-9A-Z])+)$',
        views.ResetPassword.as_view(), name='reset_password'),
    url(r'^register$', views.RegisterView.as_view(), name='register'),
    url(r'^login$', views.LoginView.as_view(), name='login'),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^community/(?P<community>\w+)$', views.CommunityView.as_view(), name='community'),
    url(r'^profile/(?P<user_id>[0-9])$', views.UserProfileDetail.as_view(), name='user_profile_detail'),
]
