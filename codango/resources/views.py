from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from resources.models import Resource
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.views.generic.base import View
# Create your views here.


class Resources(View):
    model = Resource

    def ListView(request):
        return render(request, 'resources/resources_list.html')

    def DetailView(request):
        return render(request, 'resources/resources_detail.html')

    def CreateView(request):
        fields = ['author', 'title', 'text']
        return render(request, 'resources/resources_form.html')

    def UpdateView(request):
        fields = ['author', 'title' 'text']
        return render(request, 'resources/resources_form.html')

    def DeleteView(request):
        success_url = reverse_lazy('list')
        return render(request, 'resources/resources_confirm_delete.html')


# class PdfResource(canvas):
#     if RESOURCE_TYPES == 'PDF':
#         response = HttpResponse(mimetype='application/pdf')
#         response['Content-Disposition'] = 'attachment; filename=output.pdf'

#         p = canvas.Canvas(response)

#         p.drawString(100, 100, "Hello world.")

#         p.showPage()
#         p.save()
#         return response
#         return render(request, 'account/forgot_password_reset.html')
