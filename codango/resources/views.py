import json
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import View, TemplateView
from django.template import loader
from django.db.models import Count
from resources.models import Resource
from comments.forms import CommentForm
from resources.forms import ResourceForm
from votes.models import Vote
from account.emails import SendGrid
from codango.settings.base import CODANGO_EMAIL


class LoginRequiredMixin(object):
    @method_decorator(login_required(login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(
            request, *args, **kwargs)


class CommunityBaseView(LoginRequiredMixin, TemplateView):
    template_name = 'account/home.html'

    def dispatch(self, request, *args, **kwargs):

        return super(
            CommunityBaseView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        if self.request.is_ajax():
            self.template_name = 'account/partials/community.html'

        sortby = self.request.GET[
            'sortby'] if 'sortby' in self.request.GET else 'date'

        query = self.request.GET[
            'q'] if 'q' in self.request.GET else ''

        resources = self.sort_by(sortby,
                                 Resource.objects.filter(
                                     Q(text__contains=query) |
                                     Q(snippet_text__contains=query) |
                                     Q(resource_file_name__contains=query)))

        users = User.objects.filter(
            Q(username__contains=query) |
            Q(first_name__contains=query) |
            Q(last_name__contains=query) | Q(email__contains=query))
        community = kwargs[
            'community'].upper() if 'community' in kwargs else 'ALL'

        if community == 'UNTAGGED':
            resources = resources

        elif community != 'ALL':
            resources = resources.filter(language_tags=community)

        context = {
            'resources': resources,
            'commentform': CommentForm(auto_id=False),
            'title': 'Activity Feed'
            if query == '' else query + " Search results",
            'q': query,
            'users': users
        }
        return context

    @staticmethod
    def sort_by(sorting_name, object_set):
        if sorting_name == 'date':
            return object_set.order_by('-date_modified')
        elif sorting_name == 'votes':
            results = object_set.raw(
                "SELECT resources_resource.id, votes_vote.resource_id,\
                resources_resource.date_added,\
                sum(case when votes_vote.vote=true then 1  when\
                votes_vote.vote=false then -1 else 0 end)  \
                as vote_diff from votes_vote right join resources_resource \
                on resources_resource.id = votes_vote.resource_id \
                group by votes_vote.resource_id, resources_resource.id \
                order by vote_diff desc, resources_resource.date_added desc")
            return list(results)
        else:
            return object_set.annotate(
                num_sort=Count(sorting_name)).order_by('-num_sort')


class CommunityView(CommunityBaseView):
    form_class = ResourceForm

    def post(self, request, *args, **kwargs):

        try:
            form = self.form_class(request.POST, request.FILES)
            resource = form.save(commit=False)
            try:
                resource.resource_file_name = form.files['resource_file'].name
                resource.resource_file_size = form.files['resource_file'].size
            except KeyError:
                pass
            followers = self.request.user.profile.get_following()
            resource.author = self.request.user
            resource.save()
            response_dict = {
                "content": self.request.user.username +
                " Posted a new resource",
                "link": "#",
                "type": "newpost",
                "read": False,
                "user_id": [follower.id for follower in followers],
                "status": "Successfully Posted Your Resource"
            }
            response_json = json.dumps(response_dict)
            return HttpResponse(response_json, content_type="application/json")
        except ValueError:
            return HttpResponseNotFound("emptypost")
        except:
            return HttpResponseNotFound("invalidfile")


class ResourceVoteView(View):

    def post(self, request, **kwargs):
        action = kwargs['action']
        resource_id = kwargs['resource_id']
        resource = Resource.objects.filter(id=resource_id).first()
        user_id = self.request.user.id
        vote = Vote.objects.filter(
            resource_id=resource_id, user_id=user_id).first()
        vote_mapping = {
            'likes': True,
            'unlikes': False,
        }
        # Create a vote object if the user has not voted yet
        if vote is None:
            vote = Vote()
            vote.resource = resource
            vote.user = self.request.user
        if vote.vote is None or vote.vote is not vote_mapping[action]:
            # If user has not voted yet or is changing his vote set vote to
            # current vote
            vote.vote = vote_mapping[action]
            status = action
            vote.save()
        else:
            vote.delete()
            status = "unvotes"

        response_dict = {
            "upvotes": len(resource.upvotes()),
            "downvotes": len(resource.downvotes()),
            "status": status,
        }

        if user_id != resource.author.id:
            response_dict.update(
                {"content": vote.user.username +
                    " " + status + " your resource",
                 "link": reverse(
                    'single_post', kwargs={'resource_id': vote.resource.id}),
                 "type": "vote",
                 "read": False,
                 "user_id": resource.author.id})
            if resource.author.userprofile.like_preference:
                # email here
                subject = 'Guess what ' + resource.author.username + '!'
                resource_email_context = {
                            "subject": subject,
                            "content": response_dict['content'],
                            "resource_link":
                            request.build_absolute_uri(response_dict['link']),
                            "settings_link": request.build_absolute_uri('/user/' +
                            resource.author.username + '/settings')
                        }
                message = SendGrid.compose(
                    sender='Codango <{}>'.format(CODANGO_EMAIL),
                    recipient=str(resource.author.email),
                    subject='Codango: Notification',
                    recipients=None,
                    text=loader.get_template(
                        'notifications/notification-email.txt'
                    ).render(resource_email_context),
                    html=loader.get_template(
                        'notifications/notification-email.html'
                    ).render(resource_email_context),
                )
                SendGrid.send(message)

        response_json=json.dumps(response_dict)
        return HttpResponse(response_json, content_type="application/json")


class SinglePostView(LoginRequiredMixin, TemplateView):
    template_name='resources/single-post.html'

    def get_context_data(self, **kwargs):
        context=super(SinglePostView, self).get_context_data(**kwargs)
        try:
            context['resource']=
                Resource.objects.get(id = kwargs['resource_id'])
        except Resource.DoesNotExist:
            pass
        context['commentform']=CommentForm(auto_id = False)
        context['title']='Viewing post'
        return context
