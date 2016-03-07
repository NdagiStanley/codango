from rest_framework import status
from rest_framework.test import APITestCase

message = {"detail":
           "Authentication credentials were not provided."}


class ResourceTest(APITestCase):
    """Test /api/v1/resources/ endpoint"""
    def test_resource(self):
        plain_response = self.client.get('/api/v1/resources/')
        self.assertEqual(plain_response.data, message)
        self.assertNotEqual(plain_response.data, {})
        self.assertEqual(plain_response.status_code, 401)

    """
    Will be included in the CRUD of endpoints upon authentication

    TO TEST AUTH PER URL
    token = 'JWT ' + login_response.data.get('token')
    # set authentication token in header
    self.client.credentials(HTTP_AUTHORIZATION=token)
    auth_response = self.client.post('/api/v1/....')
    """
