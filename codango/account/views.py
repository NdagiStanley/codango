from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import login

# Create your views here.


class IndexView(View):

    def get(self, request):
        return render(request, 'account/index.html')
