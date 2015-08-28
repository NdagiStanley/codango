from django.shortcuts import render

# Create your views here.
class ResourceList(ListView):
	model = Resource

class ResourceDetail(DetailView):
	model = Resource

class ResourceCreate(CreateView):
	model = Resource
	fields = ['resource_text']

class ResourceUpdate(UpdateView):
	model = Resource
	fields = ['resource_text']

class ResourceDelete(DeleteView):
	model = Resource
	success_url = reverse_lazy('resource_list')
