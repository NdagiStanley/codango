from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from resources.models import Resource
from reportlab.pdfgen import canvas
from django.http import HttpResponse
# Create your views here.


class ResourceList(ListView):
    model = Resource
    template_name = 'resources/resources_list.html'


class ResourceDetail(DetailView):
    model = Resource
    template_name = 'resources/resources_detail.html'



class ResourceCreate(CreateView):
    model = Resource
    fields = ['author', 'title', 'text']
    template_name = 'resources/resources_form.html'



class ResourceUpdate(UpdateView):
    model = Resource
    fields = ['author', 'title' 'text']


class ResourceDelete(DeleteView):
    model = Resource
    success_url = reverse_lazy('list')
