from django.conf.urls import url

from . import views

urlpatterns = [
<<<<<<< HEAD
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^home/$', views.HomeView.as_view(), name='home'),
	url(r'^recovery/$', views.ForgotPassword.as_view(), name='forgot_password')
	url(r'^recovery/$', views.ForgotPassword.as_view(), name='forgot_password'),
]