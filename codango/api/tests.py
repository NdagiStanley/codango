from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory

from django.contrib.auth.models import User


# from votes.models import Vote
# from comments.models import Comment
# from userprofile.models import UserProfile, Follow, Language, Notification
# from resources.models import Resource
# from pairprogram.models import Participant, Session


# class UserTests(APITestCase):
#     def test_create_user(self):
#         """
#         Ensure we can create a new user object.
#         """
#         # url = reverse('user-list')
#         data = {'username': 'smd', 'email': 'ndagi@gm.com', 'password': '1234'}
#         response = self.client.post('/api/v1/auth/users/', data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(User.objects.count(), 1)
#         self.assertEqual(User.objects.get().username, 'stanmd')


class ResourceTest(APITestCase):
    def test_resource(self):
        response = self.client.get('/api/v1/resources/')
        self.assertEqual(response.data, [])
        self.assertNotEqual(response.data, {})
        self.assertEqual(response.status_code, 200)


class VoteTest(APITestCase):
    def test_vote(self):
        response = self.client.get('/api/v1/votes/')
        self.assertEqual(response.data, [])
        self.assertNotEqual(response.data, {})
        self.assertEqual(response.status_code, 200)


class CommentTest(APITestCase):
    def test_comment(self):
        response = self.client.get('/api/v1/comments/')
        self.assertEqual(response.data, [])
        self.assertNotEqual(response.data, {})
        self.assertEqual(response.status_code, 200)


class ParticipantTest(APITestCase):
    def test_participants(self):
        response = self.client.get('/api/v1/pairprogram/participants/')
        self.assertEqual(response.data, [])
        self.assertNotEqual(response.data, {})
        self.assertEqual(response.status_code, 200)


class SessionTest(APITestCase):
    def test_session(self):
        response = self.client.get('/api/v1/pairprogram/sessions/')
        self.assertEqual(response.data, [])
        self.assertNotEqual(response.data, {})
        self.assertEqual(response.status_code, 200)


class UserProfileTest(APITestCase):
    def test_userprofile(self):
        response = self.client.get('/api/v1/userprofile/')
        self.assertEqual(response.data, [])
        self.assertNotEqual(response.data, {})
        self.assertEqual(response.status_code, 200)


class FollowTest(APITestCase):
    def test_follow(self):
        response = self.client.get('/api/v1/userprofile/follows/')
        self.assertEqual(response.data, [])
        self.assertNotEqual(response.data, {})
        self.assertEqual(response.status_code, 200)


class LanguageTest(APITestCase):
    def test_language(self):
        response = self.client.get('/api/v1/userprofile/languages/')
        self.assertEqual(response.data, [])
        self.assertNotEqual(response.data, {})
        self.assertEqual(response.status_code, 200)


class NotificationTest(APITestCase):
    def test_notification(self):
        response = self.client.get('/api/v1/userprofile/notifications/')
        self.assertEqual(response.data, [])
        self.assertNotEqual(response.data, {})
        self.assertEqual(response.status_code, 200)


class UserListTest(APITestCase):
    def test_userlist(self):
        response = self.client.get('/api/v1/auth/users/')
        self.assertEqual(response.data, [])
        self.assertNotEqual(response.data, {})
        self.assertEqual(response.status_code, 200)


class UserDetailTest(APITestCase):
    def test_userdetail(self):
        response = self.client.get('/api/v1/auth/users/1/')
        # import ipdb; ipdb.set_trace()
        # self.assertEqual(response.data, {})
        self.assertNotEqual(response.data, [])
        # self.assertEqual(response.status_code, 200)
