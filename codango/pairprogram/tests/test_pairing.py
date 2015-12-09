from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from pairprogram.models import Session, Participants


class PairTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.initiator = User.objects.create_user(
            username='andela',
            password='awesome'
        )
        self.initiator.set_password('awesome')
        self.initiator.save()
        self.login = self.client.login(
            username='andela', password='awesome')

        self.participant1 = User.objects.create_user(username='awesome', password='andela')
        self.participant1.set_password('andela')
        self.participant1.save()

        self.pair_session = Session.objects.create(initiator=self.initiator, session_name="SomeRandomSession")

    def test_user_can_initiate_a_pairing_session(self):
        url = reverse("pair_program", kwargs={"session_id": self.pair_session.id})
        self.client.get()




    def test_user_can_invite_another_user(self):
        pass

    def test_user_can_join_a_pairing_session(self):
        pass

    def test_pairing_participants_can_both_code(self):
        pass
