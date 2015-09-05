from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.views.generic.base import View
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from emails import send_mail
from django.http import HttpResponse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from account.hash import UserHasher
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader

# Create your views here.
class IndexView(View):
    form_class = LoginForm
    initial = {'key': 'value'}
    template_name = 'account/index.html'

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    if not request.POST.get('checkbox', None):
                        request.session.set_expiry(0)

                    login(request, user)

                    return HttpResponseRedirect('/home')

        return render(request, self.template_name, {'form': form})

class HomeView(TemplateView):
    template_name = 'account/home.html'

class ForgotPassword(View):

    def get(self, request, *args, **kwargs):
        context = {

        }
        context.update(csrf(request))
        return render(request, 'account/forgot_password.html', context)

    def post(self, request, *args, **kwargs):
        try:
            email_inputted = request.POST.get("email")
            user = User.objects.get(email = email_inputted)
            user_hash = UserHasher.gen_hash(user)
            user_hash_url = request.build_absolute_uri(reverse('reset_password', kwargs={'user_hash': user_hash}))

            hash_email_context = RequestContext(request, {'user_hash_url': user_hash_url})
            email_reponse = send_mail(
                sender = 'Codango <codango@andela.com>',
                recipient = user.email,
                subject = 'Codango: Password Recovery',
                text = loader.get_template('account/forgot_password_email.txt').render(hash_email_context),
                html = loader.get_template('account/forgot_password_email.html').render(hash_email_context),
            )
            context = {
                "email_status": email_reponse.status_code
            }
            return render(request, 'account/forgot_password_status.html', context)

        except ObjectDoesNotExist:
            messages.add_message(request, messages.INFO, 'The email specified does not belong to any valid user.')
            return render(request, 'account/forgot_password.html')


class ResetPassword(View):

    def get(self, request, *args, **kwargs):
        user_hash = kwargs['user_hash']
        user = UserHasher.reverse_hash(user_hash)

        if user is not None:
            if user.is_active:
                request.session['user_pk'] = user.pk

                context = {

                }
                context.update(csrf(request))
                return render(request, 'account/forgot_password_reset.html', context)
            else:
                messages.add_message(request, messages.ERROR, 'Account not activated!')
                return HttpResponse(
                    'Account not activated!',
                    status_code = 403,
                    reason_phrase = 'You are not allowed to view this content because your account is not activated!'
                )
        else:
            raise Http404("User does not exist")

    def post(self, request, *args, **kwargs):

        new_password = request.POST.get("password")
        try:
            user_pk = request.session['user_pk'] 
            user = User.objects.get(pk=user_pk)

            user.set_password(new_password)
            user.save()

            messages.add_message(request, messages.INFO, 'Your password was changed successfully!')

            return redirect('/account/')
        
        except ObjectDoesNotExist:
            # set an error message:
            messages.add_message(request, messages.ERROR, 'You are not allowed to perform this action!')
            return HttpResponse( 'Action not allowed!', status_code = 403 )

        context = {

        }
        context.update(csrf(request))
        return render(request, 'account/forgot_password.html', context)
