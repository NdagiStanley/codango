from django.test.utils import setup_test_environment

setup_test_environment()
from django.test import Client, TestCase
import json
import requests
from mock import Mock, patch
import requests_mock
from django.contrib.auth.models import User
from django.core.urlresolvers import resolve, reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from userprofile.models import UserProfile, Follow
from userprofile.views import FollowUserView, UserProfileEditView, UserGithub

class UserProfileTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='jubril', password='issa')
        self.user.set_password('shuaib')
        self.user.save()
        self.login = self.client.login(username='jubril', password='shuaib')

    def test_un_authenticated_user_can_see_github_link(self):
        response = self.client.get(reverse('user_profile', kwargs={'username': self.user.username}))

        self.assertIn('github_id', response.context)

    @requests_mock.mock()
    def test_user_authenticate_with_github(self, m):
        m.get('https://api.github.com/user', content='{"login":"golden0","id":7931839}')
        
        m.post('https://github.com/login/oauth/access_token', content='{"access_token":"bcddf737641265ccf43ac82fea82d29a858e87be","token_type":"bearer","scope":"public_repo,user"}')
        
        m.get('https://api.github.com/users/golden0/repos', content='[{"language": "javascript"}]')
        response = self.client.get(reverse('user_github')+'?code=ieawfeaoefaojfeaoiw')
        self.assertIsNotNone(self.user.profile.github_username)
        self.assertEqual(len(self.user.languages.all()),1)
        self.assertEqual(response.status_code, 302)

    
    @requests_mock.mock()
    def test_user_can_update_languages(self,m):
        profile = self.user.profile
        profile.github_username = "golden0"
        profile.save()
        m.get('https://api.github.com/users/golden0/repos', content='[{"language": "javascript"}]')
        response = self.client.post(reverse('user_github'))
        self.assertEqual(len(self.user.languages.all()), 1)
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


