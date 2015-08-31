from django.shortcuts import render
from django.contrib.auth import login

# Create your views here.
def index(request):
	return render(request, 'account/index.html')
