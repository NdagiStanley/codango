import json
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.contrib import messages
from django.contrib.auth.models import User
from django.template import RequestContext
from django.utils import timezone
from resources.views import LoginRequiredMixin
from comments.forms import CommentForm
from userprofile.models import UserProfile, Follow
from userprofile.forms import UserProfileForm
from resources.views import CommunityBaseView

# Create your views here.


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
        try:
            follow = Follow.objects.filter(
                follower_id=self.request.user.id).get(followed_id=user.id)
            if follow is not None:
                context['already_following'] = True
        except:
            pass

        sortby = self.request.GET[
            'sortby'] if 'sortby' in self.request.GET else 'date'

        context['resources'] = self.sort_by(sortby, user.resource_set.all())

        context['profile'] = user.profile
        context['title'] = "{}'s Feed".format(user.profile.user)
        context['commentform'] = CommentForm(auto_id=False)
        return context


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

        userprofile = UserProfile.objects.get(user_id=user.id)
        userprofile.following += 1
        userprofile.save()

        follower_user_profile = UserProfile.objects.get(
            user_id=following_id.id)
        follower_user_profile.followers += 1
        follower_user_profile.save()

        repsonse_json = {
            'no_of_followers': len(follower_user_profile.get_followers()),
            'no_following': len(follower_user_profile.get_following()),
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

        try:
            follow = Follow.objects.filter(
                follower=self.request.user.id).get(followed=user.id)

            if follow is not None:
                context['already_following'] = True
        except:
            pass

        if direction == 'followers':
            context['follower_lists'] = user_profile.get_followers()
            context['no_followers'] = 'No followers to display'
        else:
            context['following_lists'] = user_profile.get_following()
            context['no_following'] = 'Not following anyone'

        context['profile'] = user_profile
        context['resources'] = user.resource_set.all()

        return context
