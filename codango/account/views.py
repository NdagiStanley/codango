from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.contrib.auth import authenticate, login

from .forms import LoginForm
from django.views.generic.base import View
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from emails import send_mail

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
		return render(request, 'account/forgot_password.html')

	def post(self, request, *args, **kwargs):
		try:
			email_inputted = request.POST.get("email")
			user = User.object.get(email = email_inputted)
			send_mail(
				'sender' = "Codango <codango@andela.com>"
			)
		except: