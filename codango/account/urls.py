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

    # TODO: Modify format for AJAX Enabled URLs
    url(r'^ajax/community/(?P<community>\w+)$',
        views.AjaxCommunityView.as_view(), name='community'),

    
    # TODO: Move these to resource URLs
    url(r'^resource/(?P<resource_id>[0-9]+)/(?P<action>\w+)$', views.VoteAjax.as_view(), name='vote'),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),

]
