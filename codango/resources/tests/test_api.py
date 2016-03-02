from rest_framework import status
from rest_framework.test import APITestCase

message = {"detail":
           "Authentication credentials were not provided."}


class ResourceTest(APITestCase):
    def test_resource(self):
        plain_response = self.client.get('/api/v1/resources/')
        self.assertEqual(plain_response.data, message)
        self.assertNotEqual(plain_response.data, {})
        self.assertEqual(plain_response.status_code, 401)
