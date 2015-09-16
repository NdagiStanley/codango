from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from resources.models import Resource
from resources.forms import ResourceForm
from reportlab.pdfgen import canvas
from django.http import HttpResponse
# Create your views here.


# class ResourceList(ListView):
#     model = Resource
#     template_name = 'resources/resources_list.html'


# class ResourceDetail(DetailView):
#     model = Resource
#     template_name = 'resources/resources_detail.html'



class ResourceCreate(View):
    # model = Resource
    # fields = ['author', 'title', 'text']
    # template_name = 'resources/resources_form.html'
    def post(self, request):
        form = ResourceForm
        form = self.form(request.POST)
        context = {
            'page_title': 'Resources',
            'form': form,
        }
        if form.is_valid():
            resource = form.save(commit=False)
            resource.save()
            return "Hello"
        else:
            return "Nono"




# class ResourceUpdate(UpdateView):
#     model = Resource
#     fields = ['author', 'title' 'text']
#     template_name_suffix = 'resource_update_form'


# class ResourceDelete(DeleteView):
#     model = Resource
#     success_url = reverse_lazy('resources_list')
