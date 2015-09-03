from django.conf.urls import url

from . import views

urlpatterns = [
    # /account/
    url(r'^account/$', views.IndexView.as_view(), name='index'),
    # /home/
    url(r'^home/$', views.HomeView.as_view(), name='home'),

]
