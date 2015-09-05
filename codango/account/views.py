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

			email_reponse = send_mail(
				sender = 'Codango <codango@andela.com>',
				recipient = user.email,
				subject = 'Codango: Password Recovery',
				text = 'blah blah text',
				html = 'blah blah blah.html'
			)
			context = {
				"email_status": email_reponse.status_code
			}
			return render(request, 'account/forgot_password_status.html', context)

		except ObjectDoesNotExist:
			messages.add_message(request, messages.INFO, 'The email specified does not belong to any valid user.')
			return render(request, 'account/forgot_password.html')