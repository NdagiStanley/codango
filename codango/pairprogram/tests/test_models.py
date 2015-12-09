from django.test import TestCase, Client
from django.contrib.auth.models import User
from pairprogram.models import Session


class TestPairProgram(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="regularjoe", \
                                       email="regularjoe@yahoo.com", \
                                       password="regularjorpass")
        self.client = Client()
        self.client.login(username="regularjoe", password="regularjorpass")

    def test_can_create_session(self):
        pair_session = Session.objects.create(initiator=self.user, session_name="SomeRandomSession")
        self.assertIsInstance(pair_session, Session)
