from django.conf.urls import include, url
from account import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^home$', views.HomeView.as_view(), name='home'),
    url(r'^search$', views.SearchView.as_view(), name='search'),
    url(r'^search/(?P<searchby>resources|users)$',
        views.SearchView.as_view(), name='search_by'),
    url(r'^login$', views.LoginView.as_view(), name='login'),
    url(r'^about$', views.LoginView.as_view(), name='about'),
    url(r'^team$', views.LoginView.as_view(), name='team'),
    url(r'^contact$', views.LoginView.as_view(), name='contact'),
    url(r'^register$', views.RegisterView.as_view(), name='register'),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^recovery$', views.ForgotPasswordView.as_view(),
        name='forgot_password'),
    url(r'^recovery/(?P<user_hash>([a-z0-9A-Z])+)$',
        views.ResetPasswordView.as_view(), name='reset_password'),
    url('', include('social.apps.django_app.urls', namespace='social')),
]
