from django.conf.urls import url

from . import views

urlpatterns = [
    # /account/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /home/
    url(r'^$', views.HomeView.as_view(), name='home'),

]
