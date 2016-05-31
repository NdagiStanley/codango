from django.conf.urls import url, include
from account import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^home$', views.HomeView.as_view(), name='home'),
    url(r'^search$', views.SearchView.as_view(), name='search'),
    url(r'^search/(?P<searchby>resources|users)$',
        views.SearchView.as_view(), name='search_by'),
    url(r'^login$', views.LoginView.as_view(), name='login'),
    url(r'^register$', views.RegisterView.as_view(), name='register'),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^recovery$', views.ForgotPasswordView.as_view(),
        name='forgot_password'),
    url(r'^recovery/(?P<user_hash>([a-z0-9A-Z])+)$',
        views.ResetPasswordView.as_view(), name='reset_password'),
    url(r'^contact-us$', views.ContactUsView.as_view(), name='contactus'),
    url(r'^about-us$', views.AboutUsView.as_view(), name='aboutus'),
    url(r'^team$', views.TeamView.as_view(), name='team'),
    url('', include('social.apps.django_app.urls', namespace='social')),

]
