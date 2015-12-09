from django.conf.urls import url
from comments import views

urlpatterns = [
    url(r'^$', views.CommentAction.as_view(), name='new_comment'),
    url(r'^(?P<comment_id>[0-9]+)$',
        views.CommentAction.as_view(), name='comment_action'),
]
