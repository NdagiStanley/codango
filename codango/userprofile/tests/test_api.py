from rest_framework import status
from rest_framework.test import APITestCase

message = {"detail":
           "Authentication credentials were not provided."}


class UserProfileTest(APITestCase):
    """Test /api/v1/userprofile/ endpoint"""
    def test_userprofile(self):
        response = self.client.get('/api/v1/userprofile/')
        self.assertEqual(response.data, message)
        self.assertNotEqual(response.data, {})
        self.assertEqual(response.status_code, 401)


class FollowTest(APITestCase):
    """Test /api/v1/userprofile/follows/ endpoint"""
    def test_follow(self):
        response = self.client.get('/api/v1/userprofile/follows/')
        self.assertEqual(response.data, message)
        self.assertNotEqual(response.data, {})
        self.assertEqual(response.status_code, 401)


class LanguageTest(APITestCase):
    """Test /api/v1/userprofile/languages/ endpoint"""
    def test_language(self):
        response = self.client.get('/api/v1/userprofile/languages/')
        self.assertEqual(response.data, message)
        self.assertNotEqual(response.data, {})
        self.assertEqual(response.status_code, 401)


class NotificationTest(APITestCase):
    """Test /api/v1/userprofile/notifications/ endpoint"""
    def test_notification(self):
        response = self.client.get('/api/v1/userprofile/notifications/')
        self.assertEqual(response.data, message)
        self.assertNotEqual(response.data, {})
        self.assertEqual(response.status_code, 401)


    """
    Will be included in the CRUD of endpoints upon authentication

    TO TEST AUTH PER URL
    token = 'JWT ' + login_response.data.get('token')
    # set authentication token in header
    self.client.credentials(HTTP_AUTHORIZATION=token)
    auth_response = self.client.post('/api/v1/....')
    """
