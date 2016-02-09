from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from mock import patch
from pairprogram.models import Session, Participant
from account.emails import SendGrid


class PairTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.initiator = User.objects.create_user(
                username='andela',
                password='awesome',
                email='andela@andela.com'
        )
        self.user = User.objects.create_user(
                username='master',
                password='awesome',
                email='master@andela.com'
        )
        self.initiator.set_password('awesome')
        self.initiator.save()
        self.login = self.client.login(
                username='andela', password='awesome')

        self.participant1 = User.objects.create_user(
            username='awesome', password='andela')
        self.participant1.set_password('andela')
        self.participant1.save()

        self.pair_session = Session.objects.create(
            initiator=self.initiator, session_name="SomeRandomSession")

    def test_user_can_initiate_a_pairing_session(self):
        url = reverse("start_session")
        response = self.client.post(
            url, {'session_name': 'pair session with the boss'})
        self.assertEqual(response.status_code, 302)

    def test_user_can_view_current_session(self):
        url = reverse("list_sessions")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_only_participants_can_pair(self):
        url = reverse("pair_program",
                      kwargs={"session_id": self.pair_session.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_user_can_delete_his_session(self):
        url = reverse("delete_session")
        response = self.client.post(url, {
            'session_id': self.pair_session.id
        })
        self.assertEqual(response.status_code, 200)

    def test_participant_can_leave_a_session(self):
        url = reverse("delete_session")
        response = self.client.post(url, {
            'session_id': self.pair_session.id
        })
        participant = Participant.objects.all()
        self.assertEqual(len(participant), 0)


    @patch.object(SendGrid, 'send')
    def test_user_can_send_invite_to_session(self, mock_method):
        url = reverse("pair_program",
                      kwargs={"session_id": self.pair_session.id},
                      )
        response = self.client.post(
            url, {'userList[]': ['master@andela.com', 'test@yahoo.com']})
        session_participant = Participant.objects.all()
        self.assertEqual(len(session_participant), 1)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "response")
