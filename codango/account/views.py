from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import login
from .forms import LoginForm

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
            return HttpResponseRedirect('account/home.html')

        return render(request, self.template_name, {'form': form})


class HomeView(View):
    pass
