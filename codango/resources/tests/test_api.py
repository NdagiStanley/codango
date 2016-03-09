from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth.models import User
from ..models import Resource

# DRY variables to be used repeatedly
message = {"detail":
           "Authentication credentials were not provided."}
url = '/api/v1/resources/'
url_for_one = '/api/v1/resources/5'
not_found_msg = {"detail": "Not found."}

class ResourceTest(APITestCase):
    """Test /api/v1/resources/ endpoint"""

    # Include 10 resources and one user for testing purposes
    fixtures = ['resources.json']

    def setUp(self):
        # Login the user
        auth_user = {'username': User.objects.get().username,
                     'password': '1234'}
        login_response = self.client.post('/api/v1/auth/login/', auth_user)
        self.token = 'JWT ' + login_response.data.get('token')

    def test_Create_Resource(self):
        """Test Create resource"""

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

    def test_Retrieve_Resources(self):
        """Test Retrieve resources"""

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

    def test_Pagination_Resources(self):
        """Test pagination"""

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

    def test_Retrieve_specific_resource(self):
        """Test Retrieve specific resource"""

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

    def test_Update_specific_resource(self):
        """Test Update specific resource"""

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

    def test_Delete_specific_resource(self):
        """Test Delete specific resource"""

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
