from django.views.generic import View, TemplateView
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import RequestContext
from pairprogram.models import Session, Participant
from resources.views import LoginRequiredMixin
from userprofile.models import UserProfile, Follow

# Create your views here.


class StartPairView(LoginRequiredMixin, TemplateView):
    template_name = 'pairprogram/pair_invite.html'

    def get(self, request, *args, **kwargs):
        new_session = Session.objects.create(initiator=request.user)
        Participant.objects.create(participant=request.user, session_id=new_session)

        return redirect('/pair/' + str(new_session.id), context_instance=RequestContext(request))
        # return render(request, self.template_name)

    def post(self, request, **kwargs):
        pass

class PairView(LoginRequiredMixin, TemplateView):
    template_name = 'pairprogram/pair.html'

    def get(self, request, *args, **kwargs):
        context = super(PairView, self).get_context_data(**kwargs)
        participants = Participant.objects.filter(participant=self.request.user).all()

        sessions = []
        for participant in participants:
            sessions.append(Session.objects.filter(id=participant.session_id_id).get())

        context['sessions'] = sessions
        return render(request, self.template_name, context)


class PairSessionView(LoginRequiredMixin, TemplateView):

    template_name = 'pairprogram/pair_pad.html'

    def get(self, request, *args, **kwargs):
        context = super(PairSessionView, self).get_context_data(**kwargs)
        context['session_id'] = kwargs['session_id']
        participants = Participant.objects.filter(session_id=context['session_id']).all()

        # for participant in participants:
        #     print participant.participant.username + "name"

        result = any(self.request.user == x.participant for x in participants)

        if not result:
            # include a mesg
            return redirect('/home')

        return render(request, self.template_name, context)

    # def post(self, request, **kwargs):
    #
    #     session_key = request.POST.get('sessionKey')
    #     new_pair = Session(session_id=session_key)
    #     new_pair.save()
    #     return HttpResponse()
