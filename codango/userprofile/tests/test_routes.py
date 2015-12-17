from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class ProfileViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='lade',
            password='password'
        )
        self.user.set_password('password')
        self.user.save()
        self.login = self.client.login(
            username='lade', password='password')

    def test_can_reach_profile_page(self):
        response = self.client.get('/user/lade')
        self.assertEqual(response.status_code, 200)

    def test_can_reach_profile_edit_page(self):
        response = self.client.post(
            '/user/lade/edit',
            {'position': 'Software Developer',
             'place_of_work': 'Andela',
             'first_name': 'Lade',
             'last_name': 'Oshodi',
             'about': 'I love to Code'})
        self.assertEqual(response.status_code, 302)


class FollowViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(
            username='golden', password='abiodun')
        self.user2 = User.objects.create_user(
            username='jubril', password='issa')
        self.user1.save()
        self.user2.save()
        self.login = self.client.login(username='golden', password='abiodun')

    def test_can_reach_followers_page(self):
        response = self.client.get('/user/golden/followers')
        self.assertEqual(response.status_code, 200)

    def test_can_reach_following_page(self):
        response = self.client.get('/user/golden/following')
        self.assertEqual(response.status_code, 200)


class FollowUserProfileTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(
            username='golden', password='abiodun')
        self.user2 = User.objects.create_user(
            username='jubril', password='issa')
        self.user1.save()
        self.user2.save()
        self.login = self.client.login(username='golden', password='abiodun')

    def test_a_logged_in_user_can_follow_a_registered_user(self):
        response = self.client.post('/user/golden/follow')
        self.assertEqual(response.status_code, 200)


class SettingsViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='test', password='test')
        self.user.save()
        self.login = self.client.login(username='test', password='test')

    def test_can_reach_settings_page(self):
        response = self.client.get(
            reverse(
                'settings',
                kwargs={'username': self.user.username}
            ))
        self.assertEqual(response.status_code, 200)

    def test_can_change_password(self):
        response = self.client.post(
            reverse(
                'settings',
                kwargs={'username': self.user.username}
            ), {
                'new_password': 'tester',
                'verify_new_password': 'tester'
            }
        )
        # redirect with success message
        self.assertEqual(response.status_code, 302)

    def test_can_change_password_error(self):
        response = self.client.post(
            reverse(
                'settings',
                kwargs={'username': self.user.username}
            ), {
                'new_password': 'tester',
                'verify_new_password': 'tester1'
            }
        )
        # redirects with error message
        self.assertEqual(response.status_code, 302)

    def test_can_change_password_special_character_error(self):
        response = self.client.post(
            reverse(
                'settings',
                kwargs={'username': self.user.username}
            ), {
                'new_password': '??',
                'verify_new_password': '??'
            }
        )
        # redirects with error message
        self.assertEqual(response.status_code, 302)

    def test_can_change_username(self):
        response = self.client.post(
            reverse(
                'settings',
                kwargs={'username': self.user.username}
            ), {
                'new_username': 'tested'
            }
        )
        # redirects with success message
        self.assertEqual(response.status_code, 302)

    def test_can_change_username_null_error(self):
        response = self.client.post(
            reverse(
                'settings',
                kwargs={'username': self.user.username}
            ), {
                'new_username': ''
            }
        )
        # redirects with error message
        self.assertEqual(response.status_code, 302)

    def test_can_change_username_special_characters_error(self):
        response = self.client.post(
            reverse(
                'settings',
                kwargs={'username': self.user.username}
            ), {
                'new_username': '??'
            }
        )
        # redirects with error message
        self.assertEqual(response.status_code, 302)

    def test_can_set_frequency(self):
        response = self.client.post(
            reverse(
                'settings',
                kwargs={'username': self.user.username}
            ), {
                'frequency': 'daily'
            }
        )
        # redirects with success message
        self.assertEqual(response.status_code, 302)
