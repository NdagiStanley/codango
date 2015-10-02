from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, View
from resources.models import Resource
from resources.forms import ResourceForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.


class ResourceCreate(TemplateView):
    form_class = ResourceForm
    template_name = 'account/home.html'

    def get_context_data(self, **kwargs):
        context = super(ResourceCreate, self).get_context_data(**kwargs)
        context['form'] = ResourceForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        resource = form.save(commit=False)
        resource.author = self.request.user
        print resource.author
        resource.save()
        return redirect(reverse('home'))

class ResourceList(View):

    def get(self, request):
        resource_list = Resource.objects.all()
        context = {'resource_list': resource_list}
        return render(request, 'resources/list.html', context)


class ResourceDetail(View):

    def get(self, request, *args, **kwargs):
        resource_detail = Resource.objects.get(id=kwargs.get('pk'))
        context = {'resource_detail': resource_detail}
        return render(request, 'resources/detail.html', context)


class ResourceUpdate(View):

    def get(self, request, *args, **kwargs):
        resource_to_update = Resource.objects.get(id=kwargs.get('pk'))
        resource_form = ResourceForm(instance = resource_to_update)
        context = {'resource_to_update': resource_to_update, 'resource_form': resource_form}
        return render(request, 'resources/update.html', context)
    
    def post(self, request, *args, **kwargs):
        resource_to_update = Resource.objects.get(id=kwargs.get('pk'))
        resource_form = ResourceForm(request.POST, request.FILES, instance=resource_to_update)
        resource_form.author = request.user

class ResourceDelete(View):
    
    def get(self, request, *args, **kwargs):
        resource_to_delete = Resource.objects.get(id=kwargs.get('pk'))
        resource_to_delete.delete()
        return redirect(reverse('resources_list'))
