"""codango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import account.urls
import userprofile.urls
import resources.urls
import comments.urls
import pairprogram.urls
import api


urlpatterns = [
    url(r'^', include(account.urls)),
    url(r'^resource/', include(resources.urls)),
    url(r'^user/', include(userprofile.urls)),
    url(r'^comment/', include(comments.urls)),
    url(r'^pair/', include(pairprogram.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include(api)),
    url(r'^api/v1/', include('rest_framework.urls')),
    url(r'^', include('rest_framework.urls', namespace='rest_framework')),
]
