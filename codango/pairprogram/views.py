from django.core.serializers import json
from django.http import HttpResponse
from django.views.generic import View, TemplateView
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib import messages
from pairprogram.models import Session, Participant
from pairprogram.forms import SessionForm
from resources.views import LoginRequiredMixin


class StartPairView(LoginRequiredMixin, TemplateView):
    template_name = 'pairprogram/sessions.html'
    form_class = SessionForm

    def get(self, request, *args, **kwargs):
        new_session = Session.objects.create(initiator=request.user)
        new_session.session_name = new_session.initiator.username + "'s session"
        new_session.save()
        Participant.objects.create(participant=request.user, session_id=new_session.id)

        return redirect('/pair/' + str(new_session.id), context_instance=RequestContext(request))

    def post(self, request, **kwargs):

        form = self.form_class(
            request.POST, instance=request.user.profile)

        if form.is_valid():
            new_session = Session.objects.create(initiator=request.user, session_name=form.cleaned_data['session_name'])
            new_session.save()
            Participant.objects.create(participant=request.user, session_id=new_session.id)
            messages.add_message(
                request, messages.SUCCESS, 'Name Updated!')
            return redirect('/pair/' + str(new_session.id), context_instance=RequestContext(request))


class ListSessionView(LoginRequiredMixin, TemplateView):
    form_class = SessionForm
    template_name = 'pairprogram/sessions.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ListSessionView, self).get_context_data(**kwargs)
        participants = Participant.objects.filter(participant=self.request.user).all()

        sessions = []
        for participant in participants:
            sessions.append(participant.session)

        context['sessions'] = sessions
        context['sessionform'] = self.form_class()
        return context


class PairSessionView(LoginRequiredMixin, View):
    form_class = SessionForm
    template_name = 'pairprogram/editor.html'

    def get(self, request,  *args, **kwargs):
        context = {}
        context['session_id'] = kwargs['session_id']
        participants = Participant.objects.filter(session_id=context['session_id']).all()

        result = any(self.request.user == row.participant for row in participants)
        context['profile'] = self.request.user.profile
        context['session_name'] = Session.objects.get(id=context['session_id']).session_name
        context['sessionform'] = self.form_class()

        if not result:
            messages.add_message(self.request, messages.ERROR, 'No Access to this page')
            return redirect('/home', context_instance=RequestContext(self.request))

        return render(request, self.template_name, context)


class PairNameView(LoginRequiredMixin, View):
    form_class = SessionForm

    def post(self, request, **kwargs):

        form = self.form_class(
            request.POST, instance=request.user.profile)

        if form.is_valid():
            print form['session_name']
            print True
            import pdb
            pdb.set_trace()
            form.save()
            messages.add_message(
                request, messages.SUCCESS, 'Name Updated!')

        return HttpResponse(json.dumps(form), content_type="application/json")

