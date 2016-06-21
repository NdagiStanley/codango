import json
import os
import requests
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import View, TemplateView
from django.contrib import messages
from django.contrib.auth.models import User
from django.template import RequestContext
from django.utils import timezone
from resources.views import LoginRequiredMixin
from comments.forms import CommentForm
from userprofile.models import UserProfile, Follow, Notification
from userprofile.forms import UserProfileForm, ChangePasswordForm,\
    ChangeUsernameForm, NotificationPreferenceForm
from resources.views import CommunityBaseView
from django.contrib.auth import authenticate, login


# Create your views here.

CLIENT_ID = os.getenv('GITHUB_CLIENT_ID')
CLIENT_SECRET = os.getenv('GITHUB_SECRET_KEY')
HEADERS = {'Accept': 'application/json'}


class UserProfileDetailView(CommunityBaseView):
    model = UserProfile
    template_name = 'userprofile/profile.html'

    def get_context_data(self, **kwargs):
        context = super(UserProfileDetailView, self).get_context_data(**kwargs)
        username = kwargs['username']
        if self.request.user.username == username:
            user = self.request.user
        else:
            user = User.objects.get(username=username)
            if user is None:
                return Http404("User does not exist")

        sortby = self.request.GET[
            'sortby'] if 'sortby' in self.request.GET else 'date'

        context['resources'] = self.sort_by(sortby, user.resource_set.all())

        context['profile'] = user.profile
        context['title'] = "{}'s Feed".format(user.profile.user)
        context['languages'] = user.languages.all()
        context['github_id'] = CLIENT_ID
        context['commentform'] = CommentForm(auto_id=False)
        return context


class ActivityUpdate(TemplateView):
    template_name = 'userprofile/partials/activity.html'

    def get_context_data(self, **kwargs):
        context = super(ActivityUpdate, self).get_context_data(**kwargs)

        return context

    def post(self, request, *args, **kwargs):
        data = request.POST
        user = User.objects.get(id=data['user_id'])
        Notification.objects.create(
            link=data['link'], activity_type=data['type'],
            user=user, read=False, content=data['content'])

        return HttpResponse("success", content_type='text/plain')

    def put(self, request, *args, **kwargs):
        body = json.loads(request.body)
        activity = Notification.objects.filter(id=body['id']).first()
        activity.read = True
        activity.save()
        return HttpResponse("success", content_type='text/plain')

    def delete(self, request, *args, **kwargs):
        user = request.user
        user.notifications.all().delete()
        return HttpResponse("success", content_type='text/plain')


class UserGithub(View):

    def get(self, request, **kwargs):
        user = self.request.user
        code = self.request.GET['code']
        token_data = {'client_id': CLIENT_ID,
                      'client_secret': CLIENT_SECRET,
                      'code': code,
                      }

        result = requests.post(
            'https://github.com/login/oauth/access_token',
            data=token_data, headers=HEADERS)

        access_token = json.loads(result.content)['access_token']

        auth_result = requests.get(
            'https://api.github.com/user',
            headers={'Accept': 'application/json',
                     'Authorization': 'token ' + access_token},
        )
        profile = user.profile
        profile.github_username = json.loads(auth_result.content)['login']
        profile.save()
        self.update_languages(profile.github_username, user)

        messages.success(request, "Successflly authenticated with github")
        return redirect('/user/' + user.username,
                        context_instance=RequestContext(request))

    def post(self, request, **kwargs):
        user = request.user
        github_username = user.profile.github_username
        new_languages = self.update_languages(github_username, user)
        msg = 'Successfully update your languages'\
            if user.languages != new_languages\
            else 'No Update to your languages'
        messages.success(request, msg)
        return redirect('/user/' + user.username,
                        context_instance=RequestContext(request))

    @staticmethod
    def update_languages(username, user):
        repositories = requests.get(
            'https://api.github.com/users/' + username + '/repos',
            headers=HEADERS)

        repos = json.loads(repositories.content)

        for repo in repos:
            if repo['language'] is not None:
                try:
                    user.languages.create(name=repo['language'])
                except:
                    pass

        return user.languages


class UserProfileEditView(LoginRequiredMixin, TemplateView):
    form_class = UserProfileForm
    template_name = 'userprofile/profile-edit.html'

    def get_context_data(self, **kwargs):
        context = super(UserProfileEditView, self).get_context_data(**kwargs)
        username = kwargs['username']
        if self.request.user.username == username:
            user = self.request.user
        else:
            pass

        context['profile'] = user.profile
        context['resources'] = user.resource_set.all()
        context['languages'] = user.languages.all()
        context['github_id'] = CLIENT_ID
        context['profileform'] = self.form_class(initial={
            'about': self.request.user.profile.about,
            'first_name': self.request.user.profile.first_name,
            'last_name': self.request.user.profile.last_name,
            'place_of_work': self.request.user.profile.place_of_work,
            'position': self.request.user.profile.position
        })
        return context

    def post(self, request, **kwargs):
        form = self.form_class(
            request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS, 'Profile Updated!')
            return redirect(
                '/user/' + kwargs['username'],
                context_instance=RequestContext(request)
            )
        else:
            context = super(
                UserProfileEditView, self).get_context_data(**kwargs)
            context['profileform'] = self.form_class
            return render(request, self.template_name, context)


class FollowUserView(LoginRequiredMixin, View):

    def post(self, request, **kwargs):

        username = kwargs['username']
        user = User.objects.get(id=request.user.id)

        following_id = User.objects.get(username=username)
        follow = Follow(
            follower=user,
            followed=following_id,
            date_of_follow=timezone.now()
        )

        follow.save()
        repsonse_json = {
            'no_of_followers': len(following_id.profile.get_followers()),
            'no_following': len(following_id.profile.get_following()),
            'content': user.username + " follows you",
            'user_id': following_id.id,
            "link": reverse(
                'user_profile', kwargs={'username': user.username}),
            "type": "vote",
            "read": False,
        }
        json_response = json.dumps(repsonse_json)
        return HttpResponse(json_response, content_type="application/json")


class FollowListView(LoginRequiredMixin, TemplateView):
    """
    View to handle both the followers and following
    """
    template_name = 'userprofile/follow.html'

    def get_context_data(self, **kwargs):

        context = super(FollowListView, self).get_context_data(**kwargs)
        username = kwargs['username']
        direction = kwargs['direction']
        user = User.objects.get(username=username)
        user_profile = UserProfile.objects.get(user_id=user.id)

        context['follow_list'] = user_profile.get_following()\
            if direction == 'followers' else user_profile.get_followers()
        context['no_follow'] = 'No followers to display'\
            if direction == 'followers' else 'Not following anyone'
        context['direction'] = direction
        context['profile'] = user_profile
        context['github_id'] = CLIENT_ID
        context['languages'] = user.languages.all()
        context['resources'] = user.resource_set.all()

        return context


class SettingsView(LoginRequiredMixin, TemplateView):
    template_name = 'userprofile/settings.html'

    def get_context_data(self, **kwargs):
        username = self.request.user.get_username()
        user = User.objects.get(username=username)
        user_profile = UserProfile.objects.get(user_id=user.id)

        # get the current update frequency of the user
        frequency = user_profile.frequency

        context = super(SettingsView, self).get_context_data(**kwargs)
        context['profile'] = user_profile
        context['resources'] = user.resource_set.all()
        context['newusername'] = ChangeUsernameForm()
        context['notificationpreferences'] = NotificationPreferenceForm(
            initial={
            'like_preference': user_profile.like_preference,
            'comment_preference': user_profile.comment_preference})
        context['newpassword'] = ChangePasswordForm()
        context['frequency'] = frequency
        return context

    def process_new_password(self, request):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            new_password = request.POST.get('new_password')
            user = User.objects.get(id=request.user.id)
            user.set_password(new_password)
            user.save()

            # login the user again
            current_user = authenticate(
                username=request.user.get_username(),
                password=new_password)
            login(request, current_user)

            messages.add_message(
                request,
                messages.SUCCESS, 'Password changed successfully!')
        else:
            messages.error(
                request, 'Invalid input or Passwords don\'t match!')
            messages.info(
                request,
                'Only alphabetical, numeric or alphanumeric characters'
            )

    def process_new_username(self, request):
        form = ChangeUsernameForm(request.POST)
        if form.is_valid():
            new_username = request.POST.get('new_username')
            user = User.objects.get(id=request.user.id)
            user.username = new_username
            user.save()

            messages.add_message(
                request,
                messages.SUCCESS, 'Username changed successfully!')
        else:
            messages.error(
                request, 'Invalid input or Username has been taken!')
            messages.info(
                request,
                'Only alphabetical, numeric or alphanumeric characters'
            )

    def process_frequency(self, request):
        frequency = request.POST.get('frequency')
        user = UserProfile.objects.get(user_id=request.user.id)
        user.frequency = frequency
        user.save()
        messages.add_message(
            request,
            messages.SUCCESS, 'Frequency set!')

    def process_preferences(self, request):
        like_notification = request.POST.get('like_preference', False)
        comment_notification = request.POST.get('comment_preference', False)
        if like_notification == 'on':
            like_notification = True
        if comment_notification == 'on':
            comment_notification = True
        print like_notification, comment_notification
        user = UserProfile.objects.get(user_id=request.user.id)
        user.like_preference = like_notification
        user.comment_preference = comment_notification
        user.save()
        messages.add_message(
            request,
            messages.SUCCESS, 'Notification preferences set!')


    def post(self, request, **kwargs):

        if 'action' in request.POST.keys():
            action = request.POST.get('action')
            # password form
            if 'process_new_password' in action:
                self.process_new_password(request)
            # username form
            elif 'process_new_username' in action:
                self.process_new_username(request)
            # preference form
            elif 'process_preferences' in action:
                self.process_preferences(request)
            # frequency form
            elif 'process_frequency' in action:
                self.process_frequency(request)



        return redirect(reverse(
            'settings', kwargs={'username': request.user.get_username()}))
