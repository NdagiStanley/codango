from django.conf.urls import url

from . import views

urlpatterns = [
    # /
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /home/
    url(r'^home/$', views.HomeView.as_view(), name='home'),

]
