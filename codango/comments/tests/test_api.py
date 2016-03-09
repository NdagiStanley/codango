from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth.models import User
from resources.models import Resource
from comments.models import Comment

message = {"detail":
           "Authentication credentials were not provided."}
user = {'username': 'sterling',
        'email': 'archer@yahoo.com', 'password': '1234'}

url = '/api/v1/comments/'


class CommentTest(APITestCase):
    """Test /api/v1/comments/ endpoint."""

    def setUp(self):
        """Set up base details for comments endpoint."""
        # register and login a dummy user
        self.client.post('/api/v1/auth/register/', user, format='json')
        auth_user = {'username': User.objects.get().username,
                     'password': user['password']}
        login_response = self.client.post('/api/v1/auth/login/', auth_user)
        self.token = 'JWT ' + login_response.data.get('token')

        # create a dummy resource
        self.client.credentials(HTTP_AUTHORIZATION=self.token)
        resource = {'author': 1, 'text': 'some random post'}
        self.client.post('/api/v1/resources/', resource)

        # create a dummy comment
        self.comment = {'author': User.objects.get().id,
                        'content': 'finally here',
                        'resource': Resource.objects.get().id}

        self.url2 = '/api/v1/comments/1'

    def test_comment_retrieval(self):
        """Test for comment retrieval."""
        # unsuccessful comment retrieval without authentication.
        self.client.credentials(HTTP_AUTHORIZATION=' ')
        response = self.client.get(url)
        self.assertEqual(response.data, message)
        self.assertNotEqual(response.data, {})
        self.assertEqual(response.status_code, 401)

        # successful comment retrieval with authentication.
        self.client.credentials(HTTP_AUTHORIZATION=self.token)
        auth_response = self.client.get(url)
        self.assertEqual(auth_response.status_code, 200)

    def test_comment_creation(self):
        """Test for comment creation."""
        # unsuccessful comment creation without authentication.
        self.client.credentials(HTTP_AUTHORIZATION=' ')
        response = self.client.post(url)
        self.assertEqual(response.data, message)
        self.assertNotEqual(response.data, {})
        self.assertEqual(response.status_code, 401)

        # successful comment creation with authentication.
        self.client.credentials(HTTP_AUTHORIZATION=self.token)
        auth_response = self.client.post(url, self.comment)
        self.assertEqual(auth_response.status_code, 201)

    def test_comment_edition(self):
        """Test for comment update."""
        # unsuccessful comment creation without authentication.
        self.client.credentials(HTTP_AUTHORIZATION=' ')
        response = self.client.put(url)
        self.assertEqual(response.data, message)
        self.assertNotEqual(response.data, {})
        self.assertEqual(response.status_code, 401)

        # successful comment edition with authentication.
        new_comment = {'author': User.objects.get().id,
                       'content': 'Django rest framework tests.',
                       'resource': Resource.objects.get().id}
        self.client.credentials(HTTP_AUTHORIZATION=self.token)
        self.client.post(url, self.comment)
        auth_response = self.client.put(self.url2, new_comment)
        self.assertEqual(auth_response.status_code, 200)

    def test_comment_deletion(self):
        """Test for comment deletion."""
        # unsuccessful comment deletion without authentication.
        self.client.credentials(HTTP_AUTHORIZATION=' ')
        response = self.client.delete(url)
        self.assertEqual(response.data, message)
        self.assertNotEqual(response.data, {})
        self.assertEqual(response.status_code, 401)

        # successful comment deletion with authentication.
        self.client.credentials(HTTP_AUTHORIZATION=self.token)
        self.client.post(url, self.comment)
        auth_response = self.client.delete(self.url2)
        self.assertEqual(auth_response.status_code, 204)
