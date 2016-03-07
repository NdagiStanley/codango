from rest_framework import status
from rest_framework.test import APITestCase

message = {"detail":
           "Authentication credentials were not provided."}


class ParticipantTest(APITestCase):
    """Test /api/v1/pairprogram/participants/ endpoint"""
    def test_participants(self):
        response = self.client.get('/api/v1/pairprogram/participants/')
        self.assertEqual(response.data, message)
        self.assertNotEqual(response.data, {})
        self.assertEqual(response.status_code, 401)


class SessionTest(APITestCase):
    """Test /api/v1/pairprogram/sessions/ endpoint"""
    def test_session(self):
        response = self.client.get('/api/v1/pairprogram/sessions/')
        self.assertEqual(response.data, message)
        self.assertNotEqual(response.data, {})
        self.assertEqual(response.status_code, 401)
