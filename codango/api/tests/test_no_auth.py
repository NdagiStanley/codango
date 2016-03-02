from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth.models import User


message = {"detail":
           "Authentication credentials were not provided."}

class ResourceTest(APITestCase):
    def test_resource(self):
        response = self.client.get('/api/v1/resources/')
        self.assertEqual(response.data, message)
        self.assertNotEqual(response.data, {})
        self.assertEqual(response.status_code, 401)


class VoteTest(APITestCase):
    def test_vote(self):
        response = self.client.get('/api/v1/votes/')
        self.assertEqual(response.data, message)
        self.assertNotEqual(response.data, {})
        self.assertEqual(response.status_code, 401)


class CommentTest(APITestCase):
    def test_comment(self):
        response = self.client.get('/api/v1/comments/')
        self.assertEqual(response.data, message)
        self.assertNotEqual(response.data, {})
        self.assertEqual(response.status_code, 401)


class ParticipantTest(APITestCase):
    def test_participants(self):
        response = self.client.get('/api/v1/pairprogram/participants/')
        self.assertEqual(response.data, message)
        self.assertNotEqual(response.data, {})
        self.assertEqual(response.status_code, 401)


class SessionTest(APITestCase):
    def test_session(self):
        response = self.client.get('/api/v1/pairprogram/sessions/')
        self.assertEqual(response.data, message)
        self.assertNotEqual(response.data, {})
        self.assertEqual(response.status_code, 401)


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
