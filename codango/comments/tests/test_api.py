from rest_framework.test import APITestCase

from django.contrib.auth.models import User
from comments.models import Comment


# DRY variables to be used repeatedly
message = {"detail":
           "Authentication credentials were not provided."}
url = '/api/v1/resources/1/comments/'
url2 = '/api/v1/resources/1/comments/2/'
url3 = '/api/v1/resources/2/comments/'
url4 = '/api/v1/resources/2/comments/2/'
not_found_msg = {"detail": "Not found."}


class CommentsTest(APITestCase):
    """Test /api/v1/resources/<resource_id>/comments/ endpoint"""

    # Include 3 comments ,one user and one resource for testing purposes
    fixtures = ['comments.json']

    def setUp(self):
        """Set up base user and details for test running."""
        # Login the user
        auth_user = {'username': User.objects.get().username,
                     'password': 'ashley'}
        login_response = self.client.post('/api/v1/auth/login/', auth_user)
        self.token = 'JWT ' + login_response.data.get('token')

    def test_create_comment(self):
        """Test that a user can create a comment."""
        entry = {'author': 1, 'resource': 1, 'content': 'Another random post'}

        # Test unsuccessful access w/out authentication
        plain_response = self.client.post(url, entry)
        self.assertEqual(plain_response.data, message)
        self.assertNotEqual(plain_response.data, {})
        self.assertEqual(plain_response.status_code, 401)

        # set authentication token in header
        self.client.credentials(HTTP_AUTHORIZATION=self.token)
        # Post in /api/v1/resources/1/comments/ endpoint
        auth_response = self.client.post(url, entry)

        # Asserting successful access and creation of one more resource
        self.assertEqual(
            auth_response.data.get('content'), 'Another random post')
        self.assertEqual(auth_response.status_code, 201)
        self.assertNotEqual(auth_response.data, {})
        self.assertEqual(Comment.objects.count(), 4)

    def test_get_comment(self):
        """Test that a user can retrieve a comment."""
        # Test unsuccessful access without authentication
        response = self.client.get(url)
        self.assertEqual(response.data, message)
        self.assertEqual(response.status_code, 401)

        # Set authentication token
        self.client.credentials(HTTP_AUTHORIZATION=self.token)

        # Test successful retrieval of all comments.
        auth_response = self.client.get(url)
        self.assertEqual(auth_response.status_code, 200)
        self.assertEqual(auth_response.data['count'], 3)

        # Test successful retrieval of a single comment
        auth_response = self.client.get(url2)
        self.assertEqual(auth_response.status_code, 200)
        self.assertEqual(auth_response.data.get('content'), 'Lana Kane')

        # Test that no comments are returned for a resource without comments.
        auth_response = self.client.get(url3)
        self.assertEqual(auth_response.status_code, 200)
        self.assertEqual(auth_response.data['count'], 0)

    def test_edit_comment(self):
        """Test that a user can edit a comment."""
        update = {'author': 1, 'resource': 1, 'content': 'More random post'}

        # test unsuccessful update w/out authentication
        response = self.client.put(url2, update)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data, message)

        # set authentication token
        self.client.credentials(HTTP_AUTHORIZATION=self.token)

        # test successful comments update
        auth_response = self.client.put(url2, update)
        self.assertEqual(auth_response.status_code, 200)
        self.assertEqual(auth_response.data.get('content'), 'More random post')
        # check that the number of comments remains constant
        self.assertEqual(Comment.objects.count(), 3)

        # test that only comments that exist can be updated
        auth_response = self.client.put(url4, update)
        self.assertEqual(auth_response.status_code, 404)
        self.assertEqual(auth_response.data, not_found_msg)

    def test_delete_comment(self):
        """Test that a user can delete a comment."""
        # test unsuccessful update w/out authentication
        response = self.client.delete(url2)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data, message)

        # set authentication token
        self.client.credentials(HTTP_AUTHORIZATION=self.token)

        # Test successful tcomment deletion
        auth_response = self.client.delete(url2)
        self.assertEqual(auth_response.status_code, 204)
        self.assertEqual(Comment.objects.count(), 2)
