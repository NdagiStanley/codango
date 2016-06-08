import json
from django.http import HttpResponse
from django.views.generic import View
from django.core.urlresolvers import reverse

from resources.models import Resource
from comments.models import Comment
from comments.forms import CommentForm
from datetime import datetime
from django.template import loader
from account.emails import SendGrid
from codango.settings.base import CODANGO_EMAIL

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
        if comment.author.id != resource.author.id:
            response_dict = {
                "content": comment.author.username +
                " commented on your resource",
                "link": reverse('single_post',
                                kwargs={'resource_id': comment.resource.id}),
                "type": "comment",
                "read": False,
                "user_id": resource.author.id,
                "status": "Successfully Posted Your Comment for this resource"
            }
            # if resource.author.userprofile.comment_preference:
            #     # Email comes here
            subject = 'Guess what ' + resource.author.username + '!'
            comment_email_context = {
                "subject": subject,
                "content": response_dict['content'],
                "resource_link":
                    request.build_absolute_uri(response_dict['link']),
                "settings_link": request.build_absolute_uri(
                    '/user/' + resource.author.username + '/settings')
            }
                # message = SendGrid.compose(
                #     sender='Codango <{}>'.format(CODANGO_EMAIL),
                #     recipient='ndagis@gmail.com',
                #     subject='Codango: Notification',
                #     recipients=None,
                #     text=loader.get_template(
                #         'notifications/notification-email.txt'
                #     ).render(comment_email_context),
                #     html=loader.get_template(
                #         'notifications/notification-email.html'
                #     ).render(comment_email_context),
                # )
                # SendGrid.send(message)


            message = SendGrid.compose(
                'Codango <{}>'.format(CODANGO_EMAIL),
                resource.author.email,
                'Codango: Notification',
                None,
                loader.get_template('notifications/notification-email.txt'
                    ).render(comment_email_context),
                loader.get_template('notifications/notification-email.html'
                    ).render(comment_email_context),
                )
            SendGrid.send(message)


            response_json = json.dumps(response_dict)
            return HttpResponse(response_json, content_type="application/json")

        return HttpResponse("Successfully Posted Your Comment for this \
            resource", content_type='text/plain')

    def put(self, request, *args, **kwargs):
        body = json.loads(request.body)
        comment_id = kwargs['comment_id']
        comment = Comment.objects.filter(id=comment_id).first()
        comment.content = body['content']
        comment.date_modified = datetime.now()
        comment.save()
        return HttpResponse("success", content_type='text/plain')
