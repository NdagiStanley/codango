from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth.models import User


user = {'username': 'stanmd', 'email': 'ndagi@gmail.com', 'password': '1234'}
message = {"detail":
           "Authentication credentials were not provided."}

class UserTests(APITestCase):
    def test_register(self):
        """
        Ensure we can create a new user object.
        """
        # url = reverse('user-list')
        response = self.client.post('/api/v1/auth/register/', user, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'stanmd')

    def test_login(self):
        """Ensure we can login"""
        # create user
        self.client.post('/api/v1/auth/register/', user, format='json')
        # attempt login
        auth_user = {'username': User.objects.get().username,'password': user['password']}
        # Login first to get token
        login_response = self.client.post('/api/v1/auth/login/', auth_user)
        self.assertTrue('token' in login_response.data)
        self.assertEqual(login_response.status_code, 200)
        self.assertEqual(login_response.status_text, 'OK')
        self.assertNotEqual(login_response.data.get('token'), None)

        """
        TO TEST AUTH PER URL
        token = 'JWT ' + login_response.data.get('token')
        # set authentication token in header
        self.client.credentials(HTTP_AUTHORIZATION=token)
        auth_response = self.client.post('/api/v1/....')
        """

    def test_logout(self):
        """Ensure we can logout"""
        self.client.post('/api/v1/auth/register/', user, format='json')
        auth_user = {'username': User.objects.get().username,'password': user['password']}
        login_response = self.client.post('/api/v1/auth/login/', auth_user)
        self.assertTrue('token' in login_response.data)
        logout_response = self.client.post('/api/v1/auth/logout/')
        # Remove token from header
        self.client.credentials(HTTP_AUTHORIZATION=None)
        self.assertEqual(logout_response.data, message)
        self.assertEqual(logout_response.status_code, 401)


class UserListTest(APITestCase):
    def test_userlist(self):
        response = self.client.get('/api/v1/auth/users/')
        self.assertEqual(response.data, [])
        self.assertNotEqual(response.data, {})
        self.assertEqual(response.status_code, 200)


class UserDetailTest(APITestCase):
    def test_userdetail(self):
        response = self.client.get('/api/v1/auth/users/1/')
        # import ipdbgs; ipdb.set_trace()
        # self.assertEqual(response.data, {})
        self.assertNotEqual(response.data, [])
        # self.assertEqual(response.status_code, 200)
