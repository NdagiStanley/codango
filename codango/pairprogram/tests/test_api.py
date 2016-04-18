from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth.models import User
from pairprogram.models import Participant, Session


message = {"detail":
           "Authentication credentials were not provided."}
url_for_all_sessions = '/api/v1/pairprogram/sessions/'
url_for_single_session = '/api/v1/pairprogram/sessions/1/'
url_for_all_participants = '/api/v1/pairprogram/sessions/1/participants/'
url_for_single_participant = '/api/v1/pairprogram/sessions/1/participants/1/'
url_for_control_session = '/api/v1/pairprogram/sessions/4/'


class SessionTest(APITestCase):
    """Test /api/v1/pairprogram/sessions/ endpoint."""

    # plugin dummy data inclusive of one user, two sessions and 3 participants
    fixtures = ['sessions.json']

    def setUp(self):
        """Create base settings for the test class."""
        # Login the user
        auth_user = {'username': 'joan',
                     'password': 'ashley'}
        login_response = self.client.post('/api/v1/auth/login/', auth_user)
        self.token = 'JWT ' + login_response.data.get('token')

    def test_session_creation(self):
        """Test that sessions can be created."""
        # dummy session to be created
        entry = {"session_name": "trial", "initiator": 2}
        # test unsuccessful session creation w/out authentication
        response = self.client.post(url_for_all_sessions, entry)
        self.assertEqual(response.data, message)
        self.assertEqual(response.status_code, 401)

        # set authentication to the client
        self.client.credentials(HTTP_AUTHORIZATION=self.token)

        # test successful creation
        auth_response = self.client.post(url_for_all_sessions, entry)
        self.assertEqual(auth_response.status_code, 201)
        self.assertEqual(auth_response.data['session_name'], 'trial')
        self.assertEqual(Session.objects.count(), 3)

    def test_get_sessions(self):
        """Test that sessions with their details can be retrieved."""
        # test unsuccessful retrieval w/out athentication
        response = self.client.get(url_for_all_sessions)
        self.assertEqual(response.data, message)
        self.assertEqual(response.status_code, 401)

        # set authentication to the client
        self.client.credentials(HTTP_AUTHORIZATION=self.token)

        # test successful retrieval of all sessions
        auth_response = self.client.get(url_for_all_sessions)
        self.assertEqual(auth_response.status_code, 200)
        self.assertEqual(auth_response.data['count'], 2)

        # test successful retrieval of a specific session
        auth_response = self.client.get(url_for_single_session)
        self.assertEqual(auth_response.status_code, 200)
        self.assertEqual(auth_response.data['session_name'], 'hello world')

    def test_update_sessions(self):
        """Test that session details can be edited."""
        updated_entry = {"session_name": "The trials of DRF", "initiator": 2}
        # test unsuccessful edition w/out authentication
        response = self.client.put(url_for_single_session, updated_entry)
        self.assertEqual(response.data, message)
        self.assertEqual(response.status_code, 401)

        # set authentication to the client
        self.client.credentials(HTTP_AUTHORIZATION=self.token)

        # test successful update to sessions
        auth_response = self.client.put(url_for_single_session, updated_entry)
        self.assertEqual(auth_response.status_code, 200)
        self.assertEqual(
            auth_response.data['session_name'], 'The trials of DRF')

        # test that editions can only be made to existent sessions
        auth_response = self.client.put(url_for_control_session, updated_entry)
        self.assertEqual(auth_response.status_code, 404)

    def test_delete_sessions(self):
        """Test that sessions can be deleted."""
        # test unsuccessful deletion w/out authetication
        response = self.client.delete(url_for_single_session)
        self.assertEqual(response.data, message)
        self.assertEqual(response.status_code, 401)

        # set authentication to the client
        self.client.credentials(HTTP_AUTHORIZATION=self.token)

        # test successful session deletion
        auth_response = self.client.delete(url_for_single_session)
        self.assertEqual(auth_response.status_code, 204)

    def test_get_session_participants(self):
        """Test retrieval of a session's participants."""
        # test unsuccesful retrieval w/out authentication
        response = self.client.get(url_for_all_participants)
        self.assertEqual(response.data, message)
        self.assertEqual(response.status_code, 401)

        # set authentication to the client
        self.client.credentials(HTTP_AUTHORIZATION=self.token)

        # test successful participants' retrieval
        auth_response = self.client.get(url_for_all_participants)
        self.assertEqual(auth_response.status_code, 200)
        self.assertEqual(auth_response.data['count'], 2)

    def test_add_participant_to_session(self):
        """Test inivitation of a participant to a session."""
        invitee = {"participant": 1, "session": 1}
        # test unsuccessful invitation w/out authentication
        response = self.client.post(url_for_all_participants, invitee)
        self.assertEqual(response.data, message)
        self.assertEqual(response.status_code, 401)

        # set authentication to the client
        self.client.credentials(HTTP_AUTHORIZATION=self.token)

        # test successful invitation to a session
        auth_response = self.client.post(url_for_all_participants, invitee)
        self.assertEqual(auth_response.status_code, 201)
        self.assertEqual(auth_response.data['participant'], 1)
        self.assertEqual(Participant.objects.count(), 4)
        self.assertEqual(len(Participant.objects.filter(session=1)), 3)

    def test_participant_can_leave_session(self):
        """Test that a participant can leave/delete a session."""
        # test unsuccessful leave w/out authentication
        response = self.client.delete(url_for_single_participant)
        self.assertEqual(response.data, message)
        self.assertEqual(response.status_code, 401)

        # set authentication to the client
        self.client.credentials(HTTP_AUTHORIZATION=self.token)

        # test successful leave/delete with authentication
        auth_response = self.client.delete(url_for_single_participant)
        self.assertEqual(auth_response.status_code, 204)
        self.assertEqual(len(Participant.objects.filter(session=1)), 1)
