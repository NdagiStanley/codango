from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic import View, TemplateView

from comments.models import Comment
# Create your views here.

class CommentAjax(View):
	def delete(self,request, **kwargs):
		action = kwargs['action'].upper()
		comment_id = kwargs['comment_id']
		comment = Comment.objects.filter(id=comment_id).first()
		return HttpResponse(comment.content, content_type='text/plain')
        
