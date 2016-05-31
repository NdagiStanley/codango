from django.test import Client, TestCase
from navigation import NavigationMiddleWare
from mock import MagicMock
from django.contrib.auth.models import User

class NavigationMiddleWareTest(TestCase):
    ''' Testcase for the navbar sync'''
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
            id=100, username='margie', password='rain')
        self.user.set_password('rain')
        self.user.save()
        self.login = self.client.login(username='margie', password='rain')

    def test_that_middleware_updates_navbar_highlighting(self):
        ''' Test that the active bar is highlighted'''
        response = self.client.get('/home')
        self.assertEqual(response.status_code, 200)
        active_tab = response.context_data.get('active_tab')
        self.assertIsNotNone(active_tab)
        self.assertEqual(active_tab, 'home')
        response = self.client.get('/pair/')
        active_tab = response.context_data.get('active_tab')
        self.assertEqual(active_tab, 'pair')
