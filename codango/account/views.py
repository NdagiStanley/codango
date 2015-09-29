from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.contrib import messages
from telnetlib import Telnet
from django.http import HttpResponseRedirect
from django.views.generic import View, TemplateView, DetailView,UpdateView
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterForm, UserProfileForm
from django.views.generic.base import View
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
from account.hash import UserHasher
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.template.context_processors import csrf
from account.hash import UserHasher
from emails import send_mail
from resources.models import Resource
from resources.forms import ResourceForm


from account.forms import LoginForm, RegisterForm, ResetForm

from account.forms import ResetForm
from .models import UserProfile



# Create your views here.


class IndexView(TemplateView):
    initial = {'key': 'value'}
    template_name = 'account/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['loginform'] = LoginForm()
        context['registerform'] = RegisterForm()
        return context


class LoginView(IndexView):
    form_class = LoginForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if not request.POST.get('remember_me'):
                request.session.set_expiry(0)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/home')
        else:
            context = super(LoginView, self).get_context_data(**kwargs)
            context['loginform'] = form
            return render(request, self.template_name, context)


class RegisterView(IndexView):
    form_class = RegisterForm

    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            login(request, new_user)
            return HttpResponseRedirect('/home')
        else:
            context = super(RegisterView, self).get_context_data(**kwargs)
            context['registerform'] = form
            return render(request, self.template_name, context)


class HomeView(TemplateView):
    template_name = 'account/home.html'


class LoginRequiredMixin(object):
    # View mixin which requires that the user is authenticated.

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(
            request, *args, **kwargs)


class HomeView(LoginRequiredMixin, TemplateView):
    form_class = ResourceForm
    template_name = 'account/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        resource_list = reversed(Resource.objects.all())
        context = {'resource_list': resource_list}
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        resource = form.save(commit=False)
        resource.author = self.request.user
        resource.save()
        return redirect(reverse('home'))


class CommunityView(HomeView):

    def get_context_data(self, **kwargs):
        context = super(CommunityView, self).get_context_data(**kwargs)
        community = kwargs['community']
        resource_list = reversed(
            Resource.objects.filter(language_tags=community))
        context = {'resource_list': resource_list}
        return context


class ForgotPassword(View):

    def get(self, request, *args, **kwargs):
        context = {

        }
        context.update(csrf(request))
        return render(request, 'account/forgot_password.html', context)

    def post(self, request, *args, **kwargs):
        try:
            email_inputted = request.POST.get("email")
            user = User.objects.get(email=email_inputted)
            user_hash = UserHasher.gen_hash(user)
            user_hash_url = request.build_absolute_uri(
                reverse('reset_password', kwargs={'user_hash': user_hash}))

            hash_email_context = RequestContext(
                request, {'user_hash_url': user_hash_url})
            email_reponse = send_mail(
                sender='Codango <codango@andela.com>',
                recipient=user.email,
                subject='Codango: Password Recovery',
                text=loader.get_template(
                    'account/forgot_password_email.txt').render(hash_email_context),
                html=loader.get_template(
                    'account/forgot_password_email.html').render(hash_email_context),
            )
            context = {
                "email_status": email_reponse.status_code
            }
            return render(request, 'account/forgot_password_status.html', context)

        except ObjectDoesNotExist:
            messages.add_message(
                request, messages.INFO, 'The email specified does not belong to any valid user.')
            return render(request, 'account/forgot_password.html')


class ResetPassword(View):

    def get(self, request, *args, **kwargs):
        user_hash = kwargs['user_hash']
        user = UserHasher.reverse_hash(user_hash)

        if user is not None:
            if user.is_active:
                request.session['user_pk'] = user.pk

                context = {
                    "password_reset_form": ResetForm(auto_id=True)
                }
                context.update(csrf(request))
                return render(request, 'account/forgot_password_reset.html', context)
            else:
                messages.add_message(
                    request, messages.ERROR, 'Account not activated!')
                return HttpResponse(
                    'Account not activated!',
                    status_code=403,
                    reason_phrase='You are not allowed to view this content because your account is not activated!'
                )
        else:
            raise Http404("User does not exist")

    def post(self, request, *args, **kwargs):
        password_reset_form = ResetForm(request.POST, auto_id=True)
        new_password = request.POST.get("password")
        if password_reset_form.is_valid():
            try:
                user_pk = request.session['user_pk']
                user = User.objects.get(pk=user_pk)

                user.set_password(new_password)
                user.save()

                messages.add_message(
                    request, messages.INFO, 'Your password has been changed successfully!')

                return redirect('/')

            except ObjectDoesNotExist:
                # set an error message:
                messages.add_message(
                    request, messages.ERROR, 'You are not allowed to perform this action!')
                return HttpResponse('Action not allowed!', status_code=403)

        context = {
            "password_reset_form": password_reset_form
        }
        context.update(csrf(request))
        return render(request, 'account/forgot_password_reset.html', context)


class UserProfileDetailView(LoginRequiredMixin, TemplateView):
    model = UserProfile
    template_name = 'account/profile.html'
    form_class = UserProfileForm

    def post(self, request, **kwargs):
        form = self.form_class(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home')
        else:
            context = super(UserProfileDetailView, self).get_context_data(**kwargs)
            context['profileform'] = self.form_class

            print "show"
            print request.user.profile

            return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super(UserProfileDetailView, self).get_context_data( **kwargs)
        # profile = UserProfile.objects.get()
        context['profileform'] = UserProfileForm(initial={
            'place_of_work': self.request.user.profile.place_of_work,
            'position': self.request.user.profile.position,
            'followers': self.request.user.profile.followers,
            'following': self.request.user.profile.following,
        })

        context['profile'] = self.request.user.profile
        return context
