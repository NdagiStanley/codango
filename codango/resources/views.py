from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.core.urlresolvers import reverse_lazy
from resources.models import Resource
from resources.forms import ResourceForm
from reportlab.pdfgen import canvas
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User

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
        if request.user.is_authenticated():
            if form.is_valid():
                resource = form.save(commit=False)
                resource.save()
                return HttpResponseRedirect('resources/list')
            else:
                return HttpResponse('No')
        else:
            return HttpResponse('User is not active')


class ResourceList(View):

    def get(self, request, ):
        resource_list = Resource.objects.all()
        return render(request, 'resources/list.html',{'resource_list': resource_list})


class ResourceDetail(View):
    def get(self, request, *args, **kwargs):
        resource_detail = Resource.objects.get(id = kwargs.get('pk'))
        return render(request, 'resources/detail.html', {'resource_detail': resource_detail})
        