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
from userprofile.views import FollowUserView, UserProfileEditView,

class UserProfileTest(StaticLiveServerTestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='jubril', password='issa')
        self.user.set_password('shuaib')
        self.user.save()
        self.login = self.client.login(username='Abiodun', password='shuaib')


class FollowUserProfileTest(StaticLiveServerTestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(username='golden', password='abiodun')
        self.user2 = User.objects.create_user(username='jubril', password='issa')
        self.user1.save()
        self.user2.save()
        self.login = self.client.login(username='golden', password='abiodun')


    def test_a_logged_in_user_can_follow_a_registered_user(self):
      pass

