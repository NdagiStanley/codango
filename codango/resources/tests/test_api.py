from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth.models import User
from ..models import Resource

user = {'username': 'stanmd', 'email': 'ndagi@gmail.com', 'password': '1234'}
message = {"detail":
           "Authentication credentials were not provided."}


class ResourceTest(APITestCase):
    """Test /api/v1/resources/ endpoint"""

    def test_R_resource(self):
        """Test Retrieve resource"""

        url = '/api/v1/resources/'
        plain_response = self.client.get(url)
        self.assertEqual(plain_response.data, message)
        self.assertNotEqual(plain_response.data, {})
        self.assertEqual(plain_response.status_code, 401)

        # Register the user
        self.client.post('/api/v1/auth/register/', user, format='json')
        # Login the user
        auth_user = {'username': User.objects.get().username,
                     'password': user['password']}
        login_response = self.client.post('/api/v1/auth/login/', auth_user)
        token = 'JWT ' + login_response.data.get('token')

        # set authentication token in header
        self.client.credentials(HTTP_AUTHORIZATION=token)
        # Get to the resources url
        auth_response = self.client.get(url)
        self.assertEqual(auth_response.data['results'], [])
        self.assertEqual(auth_response.status_code, 200)
        self.assertNotEqual(plain_response.data, {})


    def test_C_resource(self):
        """Test Create resource"""

        url = '/api/v1/resources/'
        entry = {'author': 1, 'text': "abcdefgh", 'language_tags': "PYTHON"}
        plain_response = self.client.post(url, entry)
        self.assertEqual(plain_response.data, message)
        self.assertNotEqual(plain_response.data, {})
        self.assertEqual(plain_response.status_code, 401)

        # Register the user
        self.client.post('/api/v1/auth/register/', user, format='json')
        # Login the user
        auth_user = {'username': User.objects.get().username,
                     'password': user['password']}
        login_response = self.client.post('/api/v1/auth/login/', auth_user)
        token = 'JWT ' + login_response.data.get('token')

        # set authentication token in header
        self.client.credentials(HTTP_AUTHORIZATION=token)
        # Get to the resources url
        auth_response = self.client.post(url, entry)
        self.assertEqual(auth_response.data.get('text'), 'abcdefgh')
        self.assertEqual(auth_response.status_code, 201)
        self.assertNotEqual(plain_response.data, {})
        self.assertEqual(Resource.objects.count(), 1)


    def test_RUD_specific_resource(self):
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
