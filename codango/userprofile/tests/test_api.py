from rest_framework import status
from rest_framework.test import APITestCase

message = {"detail":
           "Authentication credentials were not provided."}


class UserProfileTest(APITestCase):
    def test_userprofile(self):
        response = self.client.get('/api/v1/userprofile/')
        self.assertEqual(response.data, message)
        self.assertNotEqual(response.data, {})
        self.assertEqual(response.status_code, 401)


class FollowTest(APITestCase):
    def test_follow(self):
        response = self.client.get('/api/v1/userprofile/follows/')
        self.assertEqual(response.data, message)
        self.assertNotEqual(response.data, {})
        self.assertEqual(response.status_code, 401)


class LanguageTest(APITestCase):
    def test_language(self):
        response = self.client.get('/api/v1/userprofile/languages/')
        self.assertEqual(response.data, message)
        self.assertNotEqual(response.data, {})
        self.assertEqual(response.status_code, 401)


class NotificationTest(APITestCase):
    def test_notification(self):
        response = self.client.get('/api/v1/userprofile/notifications/')
        self.assertEqual(response.data, message)
        self.assertNotEqual(response.data, {})
        self.assertEqual(response.status_code, 401)
