from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import View, TemplateView
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib import messages
from django.http import JsonResponse
from django.core.urlresolvers import reverse
from django.db import IntegrityError

from account.emails import SendGrid
from pairprogram.models import Session, Participant
from pairprogram.forms import SessionForm
from resources.views import LoginRequiredMixin


class StartPairView(LoginRequiredMixin, TemplateView):
    template_name = 'pairprogram/sessions.html'
    form_class = SessionForm

    def post(self, request, **kwargs):
        form = self.form_class(
                request.POST, instance=request.user.profile)

        if form.is_valid():
            new_session = Session.objects.create(
                initiator=request.user,
                session_name=form.cleaned_data['session_name'])
            new_session.save()
            Participant.objects.create(
                participant=request.user, session_id=new_session.id)
            messages.add_message(
                    request, messages.SUCCESS, 'Session started successfully')
            return redirect('/pair/' + str(new_session.id),
                            context_instance=RequestContext(request))


class ListSessionView(LoginRequiredMixin, TemplateView):
    form_class = SessionForm
    template_name = 'pairprogram/sessions.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ListSessionView, self).get_context_data(**kwargs)
        participants = Participant.objects.filter(
            participant=self.request.user).all()

        sessions = []
        for participant in participants:
            sessions.append(participant.session)

        context['sessions'] = sessions
        context['sessionform'] = self.form_class()
        return context


class PairSessionView(LoginRequiredMixin, View):
    form_class = SessionForm
    template_name = 'pairprogram/editor.html'

    def get(self, request, *args, **kwargs):
        context = {}
        context['session_id'] = kwargs['session_id']
        participants = Participant.objects.filter(
            session_id=context['session_id']).all()

        result = any(self.request.user == row.participant
                     for row in participants)
        context['profile'] = self.request.user.profile
        context['session_name'] = Session.objects.get(
            id=context['session_id']).session_name
        context['sessionform'] = self.form_class()

        if not result:
            messages.add_message(self.request, messages.ERROR,
                                 'No Access to this page')
            return redirect('/home',
                            context_instance=RequestContext(self.request))

        return render(request, self.template_name, context)

    def send_invites(self, email, session, request):
        user = User.objects.filter(email=email).first()
        if user is not None:
            try:
                Participant.objects.create(
                    participant=user, session=session)
            except IntegrityError:
                pass
            url = 'http://%s%s' % (
                    request.get_host(), reverse(
                        'pair_program', kwargs={'session_id': session.id}))
        else:
            url = 'http://%s%s?session_id=%s' % (
                request.get_host(), reverse('index'), session.id)

        message = "You've been invited to join this session please click on this <a href='{}'\
            />link </a> to join {}".format(url, session.session_name)

        email_compose = SendGrid.compose(
            sender='{} <{}>'.format(
                request.user.username, request.user.email),
            recipient=email,
            subject="Join {}".format(session.session_name),
            html=message,
            text=None
            )
        # send email
        response = SendGrid.send(email_compose)
        return response

    def post(self, request, *args, **kwargs):
        user_list = request.POST.getlist('userList[]')
        session = Session.objects.get(id=kwargs['session_id'])
        result = []
        for email in user_list:
            response_dict = {}
            response_dict['email'] = email
            response_dict['status'] = "error"
            if request.user.email != email:
                response = self.send_invites(email, session, request)
                response_dict['message'] = "Successfully sent" \
                    if response == 200 else "There was an error"
                response_dict['status'] = "success" \
                    if response == 200 else "error"

            else:
                response_dict['message'] = "You can't send an invite to yourself"
            result.append(response_dict)
        return JsonResponse(
                    {'response': result})


class DeleteSessionView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        session_id = request.POST['session_id']

        try:
            session = Session.objects.get(id=session_id)
            if session.initiator == self.request.user:
                session.delete()
            else:
                participant = Participant.objects.filter(session_id=session_id, participant_id=self.request.user)
                participant.delete()
        except Session.DoesNotExist:
            pass

        return HttpResponse('this is a response')
