from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse, Http404
from pairprogram.models import PairProgram

# Create your views here.


class PairView(TemplateView):

    template_name = 'pairprogram/pair.html'

    def get_context_data(self, **kwargs):
        context = super(PairView, self).get_context_data(**kwargs)

    def post(self, request, **kwargs):

        session_key = request.POST.get('sessionKey')
        new_pair = PairProgram(session_id=session_key)
        new_pair.save()
        return HttpResponse()