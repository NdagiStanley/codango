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
    template_name = 'resources/create.html'

    def get_context_data(self, **kwargs):
        context = super(ResourceCreate, self).get_context_data(**kwargs)
        context['form'] = ResourceForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        form.author = request.user
        if form.is_valid():
            resource = form.save(commit=False)
            resource.save()
            return redirect(reverse('resources_list'))
        else:
            return HttpResponse('No')

class ResourceList(View):

    def get(self, request):
        resource_list = Resource.objects.all()
        return render(request, 'resources/list.html', {'resource_list': resource_list})


class ResourceDetail(View):

    def get(self, request, *args, **kwargs):
        resource_detail = Resource.objects.get(id=kwargs.get('pk'))
        context = {'resource_detail': resource_detail}
        return render(request, 'resources/detail.html', context)


class ResourceUpdate(View):

    def get(self, request, *args, **kwargs):
        resource_to_update = Resource.objects.get(id=kwargs.get('pk'))
        resource_form = ResourceForm(instance = resource_to_update)
        return render(request, 'resources/update.html',
         {'resource_to_update': resource_to_update, 'resource_form': resource_form})
    
    def post(self, request, *args, **kwargs):
        resource_to_update = Resource.objects.get(id=kwargs.get('pk'))
        resource_form = ResourceForm(request.POST, request.FILES, instance=resource_to_update)
        resource_form.author = request.user

class ResourceDelete(View):
    
    def get(self, request, *args, **kwargs):
        resource_to_delete = Resource.objects.get(id=kwargs.get('pk'))
        resource_to_delete.delete()
        return redirect(reverse('resources_list'))
