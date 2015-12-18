from django.views.generic import View, TemplateView
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib import messages
from pairprogram.models import Session, Participant
from resources.views import LoginRequiredMixin
from userprofile.models import UserProfile, Follow



class StartPairView(LoginRequiredMixin, TemplateView):
    template_name = 'pairprogram/sessions.html'

    def get(self, request, *args, **kwargs):
        new_session = Session.objects.create(initiator=request.user)
        new_session.session_name = new_session.initiator.username + "'s session"
        new_session.save()
        Participant.objects.create(participant=request.user, session_id=new_session.id)

        return redirect('/pair/' + str(new_session.id), context_instance=RequestContext(request))

    # def post(self, request, **kwargs):
    #     pass


class ListSessionView(LoginRequiredMixin, TemplateView):
    
    template_name = 'pairprogram/sessions.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ListSessionView, self).get_context_data(**kwargs)
        participants = Participant.objects.filter(participant=self.request.user).all()

        sessions = []
        for participant in participants:
            sessions.append(participant.session)

        context['sessions'] = sessions
        return context


class PairSessionView(LoginRequiredMixin, View):

    template_name = 'pairprogram/editor.html'

    def get(self, request,  *args, **kwargs):
        # context = super(PairSessionView, self).get_context_data(**kwargs)
        context = {}
        context['session_id'] = kwargs['session_id']
        participants = Participant.objects.filter(session_id=context['session_id']).all()

        result = any(self.request.user == row.participant for row in participants)
        context['profile'] = self.request.user.profile

        if not result:
            # messages.add_message(
            #      messages.SUCCESS, 'Welcome back!')
            # messages.add_message(self.request, messages.ERROR, 'No Access to this page')
            return redirect('/home', context_instance=RequestContext(self.request))

        return render(request, self.template_name, context)
