import json
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic import View, TemplateView

from resources.models import Resource
from comments.models import Comment
from comments.forms import CommentForm
# Create your views here.


class CommentAction(View):

    def delete(self, request, **kwargs):
        comment_id = kwargs['comment_id']
        comment = Comment.objects.filter(id=comment_id).first()
        comment.delete()
        return HttpResponse("success", content_type='text/plain')

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        comment = form.save(commit=False)
        resource = Resource.objects.filter(
            id=request.POST.get('resource_id')).first()
        comment.resource = resource
        comment.author = self.request.user
        comment.save()

        response_dict = {
        		"content": comment.author.username + " commented on your resource",
                         "link": "http://codango-stanging/resource/1",
                         "type": "comment",
                         "read": False,
                         "user_id": resource.author.id,
                         "status": "Successfully Posted Your Commented for this resource"
                         }
        response_json = json.dumps(response_dict)
        return HttpResponse(response_json, content_type="application/json")

    def put(self, request, *args, **kwargs):
        body = json.loads(request.body)
        comment_id = kwargs['comment_id']
        comment = Comment.objects.filter(id=comment_id).first()
        comment.content = body['content']
        comment.save()
        return HttpResponse("success", content_type='text/plain')
