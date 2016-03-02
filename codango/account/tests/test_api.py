from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth.models import User

user = {'username': 'stanmd', 'email': 'ndagi@gmail.com', 'password': '1234'}
message = {"detail":
           "Authentication credentials were not provided."}


class UserTests(APITestCase):
    def test_create_user(self):
        """
        Ensure we can create a new user object.
        """
        response = self.client.post('/api/v1/auth/register/',
                                    user, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'stanmd')

    def test_login(self):
        """Ensure we can login"""
        # create user
        self.client.post('/api/v1/auth/register/', user, format='json')
        # attempt login
        auth_user = {'username': User.objects.get().username,
                     'password': user['password']}
        # Login first to get token
        login_response = self.client.post('/api/v1/auth/login/', auth_user)
        token = 'JWT ' + login_response.data.get('token')
        # set authentication token in header
        self.client.credentials(HTTP_AUTHORIZATION=token)
        auth_response = self.client.post('/api/v1/resources/')
        self.assertTrue('token' in auth_response.data)
        self.assertEqual(auth_response.status_code, 200)
        self.assertEqual(auth_response.status_text, 'OK')
        self.assertNotEqual(auth_response.data.get('token'), None)
