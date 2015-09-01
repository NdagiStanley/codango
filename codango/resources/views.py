from django.shortcuts import render
 
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from resources.models import Resource

#Create your views here.
class ResourceList(ListView):
	model = Resource

class ResourceDetail(DetailView):
	model = Resource

class ResourceCreate(CreateView):
	model = Resource
	fields = ['author', 'title', 'text']

class ResourceUpdate(UpdateView):
	model = Resource
	fields = ['author', 'title' 'text']

class ResourceDelete(DeleteView):
	model = Resource
	success_url = reverse_lazy('list')
