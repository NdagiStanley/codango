from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import RequestContext
from pairprogram.models import Session, Participant
from account.views import LoginRequiredMixin
from userprofile.models import UserProfile, Follow

# Create your views here.


class PairView(LoginRequiredMixin, TemplateView):

    template_name = 'pairprogram/pair_program.html'

    def get(self, request, *args, **kwargs):
        context = super(PairView, self).get_context_data(**kwargs)
        session_id = kwargs['session_id']
        participants = Participant.objects.filter(session_id=session_id).all()

        # for participant in participants:
        #     print participant.participant.username + "name"

        result = any(self.request.user == x.participant for x in participants)

        if not result:
            return redirect('/home')

        return render(request, self.template_name, context)

    # def post(self, request, **kwargs):
    #
    #     session_key = request.POST.get('sessionKey')
    #     new_pair = Session(session_id=session_key)
    #     new_pair.save()
    #     return HttpResponse()