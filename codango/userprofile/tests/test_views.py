from django.test.utils import setup_test_environment

setup_test_environment()
from django.test import Client, TestCase
import json
from django.contrib.auth.models import User
from django.core.urlresolvers import resolve, reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from userprofile.models import UserProfile, Follow
from userprofile.views import FollowUserView, UserProfileEditView, CLIENT_ID

class UserProfileTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='jubril', password='issa')
        self.user.set_password('shuaib')
        self.user.save()
        self.login = self.client.login(username='jubril', password='shuaib')

    def test_user_can_reach_profile_page(self):
        response = self.client.get(reverse('user_profile', kwargs={'username': self.user.username}))

        self.assertIn('github_id', response.context)
    def test_user_can_update_languages(self):
        profile = self.user.profile
        profile.github_username = "golden0"
        profile.save()
        response = self.client.post(reverse('user_github'))
        self.assertGreater(self.user.languages.all(), 1)
        self.assertEqual(response.status_code, 302)

class FollowUserProfileTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(username='golden', password='abiodun')
        self.user2 = User.objects.create_user(username='jubril', password='issa')
        self.user1.save()
        self.user2.save()
        self.login = self.client.login(username='golden', password='abiodun')

    def test_a_logged_in_user_can_follow_a_registered_user(self):
        response =self.client.post('/user/golden/follow')
        self.assertEqual(response.status_code, 200)


