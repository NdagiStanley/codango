import json
from django.http import HttpResponse
from django.views.generic import View

from resources.models import Resource
from comments.models import Comment
from comments.forms import CommentForm
from datetime import datetime
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
        comment.resource = Resource.objects.filter(
            id=request.POST.get('resource_id')).first()
        comment.author = self.request.user
        comment.save()
        return HttpResponse("success", content_type='text/plain')

    def put(self, request, *args, **kwargs):
        body = json.loads(request.body)
        comment_id = kwargs['comment_id']
        comment = Comment.objects.filter(id=comment_id).first()
        comment.content = body['content']
        comment.date_modified = datetime.now()
        comment.save()
        return HttpResponse("success", content_type='text/plain')
