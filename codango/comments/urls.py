from django.conf.urls import url
from comments import views

urlpatterns = [
url(r'^/(?P<comment_id>[0-9]+)/(?P<action>\w+)$', views.CommentAjax.as_view(), name='comment'),
]

