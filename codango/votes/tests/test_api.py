from rest_framework import status
from rest_framework.test import APITestCase

message = {"detail":
           "Authentication credentials were not provided."}


class VoteTest(APITestCase):
    """Test /api/v1/votes/ endpoint"""
    def test_vote(self):
        response = self.client.get('/api/v1/votes/')
        self.assertEqual(response.data, message)
        self.assertNotEqual(response.data, {})
        self.assertEqual(response.status_code, 401)
