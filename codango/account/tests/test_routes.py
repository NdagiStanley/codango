from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.urlresolvers import resolve
from account import urls
from account.views import ForgotPassword, ResetPassword



class IndexViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        User.objects.create_user(
            username='lade',
            password='password'
        )

    def test_can_reach_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_right_view_for_index_is_returned(self):
        match = resolve('/')
        self.assertEqual(match.url_name, 'index')

    def test_can_login(self):
        response = self.client.post('/', {
            'username': 'lade',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 302)


class HomeViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_can_reach_home_page(self):
        response = self.client.get('/home')
        self.assertEqual(response.status_code, 301)

    def test_right_view_for_home_is_returned(self):
        match = resolve('/home/')
        self.assertEqual(match.url_name, 'home')

class ForgotResetTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_forgot_route_resolves_to_correct_view(self):
        response = self.client.get('/recovery/')
        self.assertEqual(response.resolver_match.func.__name__, ForgotPassword.as_view().__name__)

    def test_reset_route_resolves_to_correct_view(self):
        response = self.client.get('/recovery/ajkzfYba9847DgJ7wbkwAaSbkTjUdawGG998qo3HG8qae83')
        self.assertEqual(response.resolver_match.func.__name__, ResetPassword.as_view().__name__)
