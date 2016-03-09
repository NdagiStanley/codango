from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth.models import User
from ..models import Resource

# DRY variables to be used repeatedly
user = {'username': 'stanmd', 'email': 'ndagi@gmail.com', 'password': '1234'}
message = {"detail":
           "Authentication credentials were not provided."}
url = '/api/v1/resources/'
url_for_one = '/api/v1/resources/5'
not_found_msg = {"detail": "Not found."}

class ResourceTest(APITestCase):
    """Test /api/v1/resources/ endpoint"""

    def setUp(self):
        # Register the user
        self.client.post('/api/v1/auth/register/', user, format='json')
        # Login the user
        auth_user = {'username': User.objects.get().username,
                     'password': user['password']}
        login_response = self.client.post('/api/v1/auth/login/', auth_user)
        self.token = 'JWT ' + login_response.data.get('token')

    def test_C_resource(self):
        """Test Create resource"""

        entry = {'author': 1, 'text': "abcdefgh", 'language_tags': "PYTHON"}
        plain_response = self.client.post(url, entry)
        self.assertEqual(plain_response.data, message)
        self.assertNotEqual(plain_response.data, {})
        self.assertEqual(plain_response.status_code, 401)

        # set authentication token in header
        self.client.credentials(HTTP_AUTHORIZATION=self.token)
        auth_response = self.client.post(url, entry)

        self.assertEqual(auth_response.data.get('text'), 'abcdefgh')
        self.assertEqual(auth_response.status_code, 201)
        self.assertNotEqual(auth_response.data, {})
        self.assertEqual(Resource.objects.count(), 1)

    def test_R_resource(self):
        """Test Retrieve resources"""

        plain_response = self.client.get(url)
        self.assertEqual(plain_response.data, message)
        self.assertNotEqual(plain_response.data, {})
        self.assertEqual(plain_response.status_code, 401)

        # set authentication token in header
        self.client.credentials(HTTP_AUTHORIZATION=self.token)
        auth_response = self.client.get(url)

        self.assertEqual(auth_response.data['results'], [])
        self.assertEqual(auth_response.status_code, 200)
        self.assertNotEqual(auth_response.data, {})

    def test_pagination_resource(self):
        """Test pagination"""

        # set authentication token in header
        self.client.credentials(HTTP_AUTHORIZATION=self.token)
        # Create several resources
        for i in range(10):
            entry = {'author': User.objects.get().id,
                     'text': "Resource%d" % i,
                     'language_tags': "PYTHON"}
            self.client.post(url, entry)
        auth_response = self.client.get(url)

        # According to the number specified in the settings/base.py
        self.assertEqual(auth_response.data['count'], 10)
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

    def test_R_specific_resource(self):
        """Test Retrieve specific resource"""
        plain_response = self.client.get(url_for_one)
        self.assertEqual(plain_response.data, message)
        self.assertNotEqual(plain_response.data, {})
        self.assertEqual(plain_response.status_code, 401)

        # set authentication token in header
        self.client.credentials(HTTP_AUTHORIZATION=self.token)
        auth_response = self.client.get(url_for_one)

        self.assertEqual(auth_response.data, not_found_msg)
        self.assertEqual(auth_response.status_code, 404)
        self.assertNotEqual(auth_response.data, {})

        # Create several resources
        for i in range(10):
            entry = {'author': User.objects.get().id,
                     'text': "Resource%d" %i,
                     'language_tags': "PYTHON"}
            self.client.post(url, entry)
        auth_response = self.client.get(url_for_one)
        self.assertNotEqual(auth_response.data, not_found_msg)
        self.assertEqual(auth_response.status_code, 200)
        self.assertEqual(auth_response.data.get('text'), 'Resource4')

    def test_U_specific_resource(self):
        """Test Update specific resource"""

        update_info = {"author": 1, "text": "Test Update",
                       "language_tags": "PYTHON", "resource_file": 'None',
                       "resource_file_name": 'None', "resource_file_size": 0,
                       "snippet_text": "random Text",
                       "date_added": "2016-03-01T13:54:52.326929Z",
                       "date_modified": "2016-03-01T13:54:52.326965Z"}
        plain_response = self.client.put(url_for_one, update_info)
        self.assertEqual(plain_response.data, message)
        self.assertNotEqual(plain_response.data, {})
        self.assertEqual(plain_response.status_code, 401)

        # set authentication token in header
        self.client.credentials(HTTP_AUTHORIZATION=self.token)
        # Get to the specific resources url
        auth_response = self.client.get(url_for_one)

        self.assertEqual(auth_response.data, not_found_msg)
        self.assertEqual(auth_response.status_code, 404)
        self.assertNotEqual(auth_response.data, {})

        # Create several resources
        for i in range(10):
            entry = {'author': User.objects.get().id,
                     'text': "Resource%d" % i,
                     'language_tags': "PYTHON"}
            self.client.post('/api/v1/resources/', entry)
        auth_response = self.client.put(url_for_one, update_info)
        self.assertNotEqual(auth_response.data, not_found_msg)
        self.assertEqual(auth_response.status_code, 200)
        self.assertNotEqual(auth_response.data.get('text'), 'Resource4')
        self.assertEqual(auth_response.data.get('text'), 'Test Update')

    def test_D_specific_resource(self):
        """Test Delete specific resource"""

        plain_response = self.client.delete(url_for_one)
        self.assertEqual(plain_response.data, message)
        self.assertNotEqual(plain_response.data, {})
        self.assertEqual(plain_response.status_code, 401)

        # set authentication token in header
        self.client.credentials(HTTP_AUTHORIZATION=self.token)
        auth_response = self.client.get(url_for_one)

        self.assertEqual(auth_response.data, not_found_msg)
        self.assertEqual(auth_response.status_code, 404)
        self.assertNotEqual(auth_response.data, {})

        # Create several resources
        for i in range(10):
            entry = {'author': User.objects.get().id,
                     'text': "Resource%d" % i,
                     'language_tags': "PYTHON"}
            self.client.post('/api/v1/resources/', entry)
        auth_response = self.client.delete(url_for_one)
        self.assertEqual(auth_response.data, None)
        self.assertEqual(self.client.get(url).data['count'], 9)
        self.assertEqual(auth_response.status_code, 204)
