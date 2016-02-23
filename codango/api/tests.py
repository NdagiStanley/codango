from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory
from votes.models import Vote
from comments.models import Comment
from userprofile.models import UserProfile, Follow, Language, Notification
from resources.models import Resource
from pairprogram.models import Participant, Session

class ResourceTest(APITestCase):
    def testresource(self):
        response = self.client.get('/api/v1/resources/')
        self.assertEqual(response.data, [])
        self.assertNotEqual(response.data, {})

class VoteTest(APITestCase):
    def testvote(self):
        response = self.client.get('/api/v1/votes/')
        self.assertEqual(response.data, [])
        self.assertNotEqual(response.data, {})

class CommentTest(APITestCase):
    def testcomment(self):
        response = self.client.get('/api/v1/comments/')
        self.assertEqual(response.data, [])
        self.assertNotEqual(response.data, {})

class ParticipantTest(APITestCase):
    def testparticipants(self):
        response = self.client.get('/api/v1/pairprogram/participants/')
        self.assertEqual(response.data, [])
        self.assertNotEqual(response.data, {})

class SessionTest(APITestCase):
    def testsession(self):
        response = self.client.get('/api/v1/pairprogram/sessions/')
        self.assertEqual(response.data, [])
        self.assertNotEqual(response.data, {})

class UserProfileTest(APITestCase):
    def testuserprofile(self):
        response = self.client.get('/api/v1/userprofile/')
        self.assertEqual(response.data, [])
        self.assertNotEqual(response.data, {})

class FollowTest(APITestCase):
    def testfollow(self):
        response = self.client.get('/api/v1/userprofile/follows/')
        self.assertEqual(response.data, [])
        self.assertNotEqual(response.data, {})

class LanguageTest(APITestCase):
    def testlanguage(self):
        response = self.client.get('/api/v1/userprofile/languages/')
        self.assertEqual(response.data, [])
        self.assertNotEqual(response.data, {})

class NotificationTest(APITestCase):
    def testnotification(self):
        response = self.client.get('/api/v1/userprofile/notifications/')
        self.assertEqual(response.data, [])
        self.assertNotEqual(response.data, {})
