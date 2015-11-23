from django.conf import settings
from django.conf.urls import url
from account import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^home$', views.HomeView.as_view(), name='home'),
    url(r'^login$', views.LoginView.as_view(), name='login'),
    url(r'^register$', views.RegisterView.as_view(), name='register'),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^recovery$', views.ForgotPasswordView.as_view(),
        name='forgot_password'),
    url(r'^recovery/(?P<user_hash>([a-z0-9A-Z])+)$',
        views.ResetPasswordView.as_view(), name='reset_password'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
    url(r'^contact-us$', views.ContactUsView.as_view(), name='contactus'),
]
