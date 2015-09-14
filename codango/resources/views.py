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
    return render(request, 'resources/resources_list.html')


class ResourceDetail(DetailView):
    model = Resource
    return render(request, 'resources/resources_detail.html')


class ResourceCreate(CreateView):
    model = Resource
    fields = ['author', 'title', 'text']
    return render(request, 'resources/resources_form.html')


class ResourceUpdate(UpdateView):
    model = Resource
    fields = ['author', 'title' 'text']
    return render(request, 'resources/resources_form.html')



class ResourceDelete(DeleteView):
    model = Resource
    success_url = reverse_lazy('list')
    return render(request, 'resources/resources_confirm_delete.html')



class PdfResource(canvas):
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=output.pdf'

    p = canvas.Canvas(response)

    p.drawString(100, 100, "Hello world.")

    p.showPage()
    p.save()
    return response
    return render(request, 'account/forgot_password_reset.html')
