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
from userprofile.models import UserProfile, Follow, Notification
from userprofile.views import FollowUserView, UserProfileEditView, UserGithub

class UserProfileTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.PhantomJS()
        self.browser.set_window_size(1400, 1000)
        self.browser.implicitly_wait(10)
        self.browser.get(self.live_server_url)

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Codango', body.text)
        self.client = Client()
        self.user = User.objects.create(id=100,username='jubril', password='issa')
        self.user.set_password('shuaib')
        self.user.save()
        self.login = self.client.login(username='jubril', password='shuaib')
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('lade')
        self.notification = Notification.objects.create(id=100,content="Python",
                                                        user=self.user, read=False, link="link",
                                                        activity_type="Vote")

    def tearDown(self):
        self.browser.quit()


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

    def test_user_can_view_activity(self):
        response = self.client.get(reverse('user_activity'))
        self.assertEqual(response.status_code,200)

    def test_user_can_post_activities(self):
        response = self.client.post(reverse('user_activity'),
                                    {'user_id':100,
                                        'content': "brand new",
                                        'link': "link",
                                        'type': "vote"},
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "success")

    def test_user_can_read_comments(self):
        json_data = json.dumps({'id': '100', })
        response = self.client.put(reverse('user_activity'), json_data, content_type='application/json',
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "success")

class FollowUserProfileTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(username='golden', password='abiodun')
        self.user2 = User.objects.create_user(username='jubril', password='issa')
        self.user1.save()
        self.user2.save()
        self.login = self.client.login(username='golden', password='abiodun')

        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('password')
        password_field.send_keys(Keys.RETURN)

        # username and password accepted
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Share', body.text)

        # User profile
        self.browser.find_element_by_link_text('lade').click()
        self.browser.find_element_by_link_text('View Profile').click()
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('@lade', body.text)


class SettingsPageTest(StaticLiveServerTestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.browser = webdriver.PhantomJS()
        self.browser.set_window_size(1400, 1000)
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    def test_can_reach_settings_page(self):
        self.browser.get(self.live_server_url)

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Codango', body.text)

        # logging in username and password
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('lade')

        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('password')
        password_field.send_keys(Keys.RETURN)

        # username and password accepted
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Share', body.text)

        # Settings page
        self.browser.find_element_by_link_text('lade').click()
        self.browser.find_element_by_link_text('Settings').click()
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Manage your Settings', body.text)

        # Change password
        password_field = self.browser.find_element_by_name('new_password')
        password_field.send_keys('pass')
        password_field = self.browser.find_element_by_name(
            'verify_new_password')
        password_field.send_keys('pass')
        password_field.send_keys(Keys.RETURN)
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Manage your Settings', body.text)

        # Change username
        username_field = self.browser.find_element_by_name('new_username')
        username_field.send_keys('laddeos')
        username_field.send_keys(Keys.RETURN)
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Manage your Settings', body.text)
