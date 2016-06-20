from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth.models import User
from ..models import Resource

# DRY variables to be used repeatedly
message = {"detail":
           "Authentication credentials were not provided."}
url = '/api/v1/resources/'
url_for_one = '/api/v1/resources/5/'
not_found_msg = {"detail": "Not found."}


class ResourceTest(APITestCase):
    """Test /api/v1/resources/ endpoint."""

    # Include 10 resources and one user for testing purposes
    fixtures = ['resources.json']

    def setUp(self):
        # Login the user
        auth_user = {'username': User.objects.get().username,
                     'password': '1234'}
        login_response = self.client.post('/api/v1/auth/login/', auth_user)
        self.token = 'JWT ' + login_response.data.get('token')

    def test_create_resource(self):
        """Test Create resource."""
        entry = {'author': 1, 'text': "abcdefgh", 'language_tags': "PYTHON"}

        # Test FALSE access w/out authentication
        plain_response = self.client.post(url, entry)
        self.assertEqual(plain_response.data, message)
        self.assertNotEqual(plain_response.data, {})
        self.assertEqual(plain_response.status_code, 401)

        # set authentication token in header
        self.client.credentials(HTTP_AUTHORIZATION=self.token)
        # Post in /api/v1/resources/ endpoint
        auth_response = self.client.post(url, entry)

        # Asserting TRUE access and creation of one more resource
        self.assertEqual(auth_response.data.get('text'), 'abcdefgh')
        self.assertEqual(auth_response.status_code, 201)
        self.assertNotEqual(auth_response.data, {})
        self.assertEqual(Resource.objects.count(), 11)

    def test_retrieve_resources(self):
        """Test Retrieve resources."""
        # Test FALSE access w/out authentication
        plain_response = self.client.get(url)
        self.assertEqual(plain_response.data, message)
        self.assertNotEqual(plain_response.data, {})
        self.assertEqual(plain_response.status_code, 401)

        # set authentication token in header
        self.client.credentials(HTTP_AUTHORIZATION=self.token)

        # Asserting TRUE access
        auth_response = self.client.get(url)
        self.assertEqual(auth_response.data['count'], 10)
        self.assertEqual(auth_response.status_code, 200)
        self.assertNotEqual(auth_response.data, {})

    def test_pagination_resources(self):
        """Test pagination."""
        # set authentication token in header
        self.client.credentials(HTTP_AUTHORIZATION=self.token)
        auth_response = self.client.get(url)

        # Assert pagination The number is specified in the settings/base.py
        self.assertEqual(auth_response.data['next'],
                         "http://testserver/api/v1/resources/?page=2")
        # Null in JSON is equal to None in Python
        self.assertEqual(auth_response.data['previous'], None)
        self.assertEqual(len(auth_response.data['results']), 3)
        self.assertEqual(auth_response.status_code, 200)
        self.assertNotEqual(auth_response.data, {})
        next_page_url = '/api/v1/resources/?page=2'
        self.assertEqual(self.client.get(next_page_url).data['next'],
                         "http://testserver/api/v1/resources/?page=3")
        self.assertEqual(self.client.get(next_page_url).data['previous'],
                         "http://testserver/api/v1/resources/")
        self.assertEqual(len(auth_response.data['results']), 3)

    def test_retrieve_specific_resource(self):
        """Test Retrieve specific resource."""
        # Test FALSE access w/out authentication
        plain_response = self.client.get(url_for_one)
        self.assertEqual(plain_response.data, message)
        self.assertNotEqual(plain_response.data, {})
        self.assertEqual(plain_response.status_code, 401)

        # set authentication token in header
        self.client.credentials(HTTP_AUTHORIZATION=self.token)
        # Get to the specific resources url
        auth_response = self.client.get(url_for_one)

        # Asserting TRUE access and retrieval of one resource
        self.assertNotEqual(auth_response.data, not_found_msg)
        self.assertEqual(auth_response.status_code, 200)
        self.assertEqual(auth_response.data.get('text'), 'Resource5')

    def test_update_specific_resource(self):
        """Test Update specific resource."""
        update_info = {"author": 1, "text": "Test Update",
                       "language_tags": "PYTHON", "resource_file": 'None',
                       "resource_file_name": 'None', "resource_file_size": 0,
                       "snippet_text": "random Text",
                       "date_added": "2016-03-01T13:54:52.326929Z",
                       "date_modified": "2016-03-01T13:54:52.326965Z"}

        # Test FALSE access w/out authentication
        plain_response = self.client.put(url_for_one, update_info)
        self.assertEqual(plain_response.data, message)
        self.assertNotEqual(plain_response.data, {})
        self.assertEqual(plain_response.status_code, 401)

        # set authentication token in header
        self.client.credentials(HTTP_AUTHORIZATION=self.token)
        # Update at the specific resources url
        auth_response = self.client.put(url_for_one, update_info)

        # Asserting TRUE access and update of specified resource
        self.assertEqual(auth_response.status_code, 200)
        self.assertNotEqual(auth_response.data.get('text'), 'Resource5')
        self.assertNotEqual(auth_response.data.get('language_tags'), 'PHP')
        self.assertEqual(auth_response.data.get('text'), 'Test Update')
        self.assertEqual(auth_response.data.get('language_tags'), 'PYTHON')

    def test_delete_specific_resource(self):
        """Test delete specific resource."""
        # Test FALSE access w/out authentication
        plain_response = self.client.delete(url_for_one)
        self.assertEqual(plain_response.data, message)
        self.assertNotEqual(plain_response.data, {})
        self.assertEqual(plain_response.status_code, 401)

        # set authentication token in header
        self.client.credentials(HTTP_AUTHORIZATION=self.token)
        # Delete at the specific resources url
        auth_response = self.client.delete(url_for_one)

        # Asserting TRUE access and deletion of one resource
        self.assertEqual(auth_response.data, None)
        self.assertEqual(auth_response.status_code, 204)
        self.assertEqual(self.client.get(url).data['count'], 9)


class ResourceVoteTest(APITestCase):
    """Test /api/v1/resources/<resource_id>/vote endpoint."""


    def setUp(self):
        # Login the user
        self.create_user()
        auth_user = {'username': self.user.username,
                     'password': '1234'}
        login_response = self.client.post('/api/v1/auth/login/', auth_user)
        self.token = 'JWT ' + login_response.data.get('token')
         # set authentication token in header
        self.client.credentials(HTTP_AUTHORIZATION=self.token)
        self.create_resource()

    def create_user(self):
        user = User(username= 'sundayguru')
        user.set_password('1234')
        user.save()
        self.user = user

    def create_resource(self):
        entry = {'author': 1, 'text': "abcdefgh", 'language_tags': "PYTHON"}
        response = self.client.post(url, entry)
        self.vote_url = url + str(response.data.get('id', 0)) + '/votes/'

    def create_vote(self, status):
        entry = {'vote': status}
        return self.client.post(self.vote_url, entry)

    def test_like_resource(self):
        response = self.create_vote(True)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data.get('vote'), True)


    def test_remove_like_resource(self):
        response = self.create_vote(True)
        self.assertEqual(response.data.get('vote'), True)

        response = self.create_vote(True)
        self.assertEqual(response.data.get('id'), None)

    def test_change_like_to_unlike_resource(self):
        response = self.create_vote(True)
        self.assertEqual(response.data.get('vote'), True)
        vote_id = response.data.get('id')

        response = self.create_vote(False)
        self.assertEqual(response.data.get('vote'), False)
        self.assertEqual(response.data.get('id'), vote_id)

    def test_unlike_resource(self):
        response = self.create_vote(False)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data.get('vote'), False)

    def test_remove_unlike_resource(self):
        response = self.create_vote(False)
        self.assertEqual(response.data.get('vote'), False)

        response = self.create_vote(False)
        self.assertEqual(response.data.get('id'), None)


    def test_change_unlike_to_like_resource(self):
        response = self.create_vote(False)
        self.assertEqual(response.data.get('vote'), False)
        vote_id = response.data.get('id')

        response = self.create_vote(True)
        self.assertEqual(response.data.get('vote'), True)
        self.assertEqual(response.data.get('id'), vote_id)

    def test_get_resource_votes(self):
        self.create_vote(True)

        response = self.client.get(self.vote_url)
        self.assertEqual(response.status_code, 200)
        votes = response.data.get('results')
        self.assertEqual(len(votes), 1)


