from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from resources.models import Resource
from resources.forms import ResourceForm
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
# photo = models.ImageField(storage=fs)

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
                return HttpResponse('Yes')
            else:
                return HttpResponse('No')
        else:
            return HttpResponse('User is not active')
        return render(request, 'resources/list.html')


class ResourceList(ListView):
    template_name = 'resources/list.html'
    model = Resource

    # def get(self):
    #     pass
    


# class ResourceDetail(DetailView):
#     model = Resource
#     template_name = 'resources/resources_detail.html'


# class ResourceUpdate(UpdateView):
#     model = Resource
#     fields = ['author', 'title' 'text']
#     template_name_suffix = 'resource_update_form'


# class ResourceDelete(DeleteView):
#     model = Resource
#     success_url = reverse_lazy('resources_list')
