from django.test.utils import setup_test_environment
setup_test_environment()
from django.test import Client, TestCase
import json
from django.contrib.auth.models import User
from django.core.urlresolvers import resolve, reverse

from resources.models import Resource
from votes.models import Vote


class CommunityViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='Abiodun', password='shuaib')
        self.user.set_password('shuaib')
        self.user.save()
        self.login = self.client.login(username='Abiodun', password='shuaib')

    def create_resources(self, text='some more words', resource_file='resource_file'):
        return Resource.objects.create(id=100, text=text, author=self.user, resource_file=resource_file)

    def test_can_reach_ajax_community_page(self):
        self.assertTrue(self.login)
        response = self.client.get(reverse('community', args=('all',)), content_type='application/json',
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertTrue(response.status_code == 200)
        self.assertContains(response, "There are currently no posts")

    def test_can_post_new_ajax_content(self):
        self.assertTrue(self.login)
        response = self.client.post('/resource/create',
                                    {'text': '1', },
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "success")

    def test_add_an_empty_resource(self):
        self.assertTrue(self.login)
        response = self.client.post('/resource/newresource',
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 404)

    def test_user_can_upvote(self):
        self.assertTrue(self.login)
        resource = self.create_resources()
        response = self.client.post('/resource/100/like', {'resource_id': 100},
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(resource.upvotes()), 1)

    def test_user_can_downvote(self):
        self.assertTrue(self.login)
        resource = self.create_resources()
        response = self.client.post('/resource/100/unlike', {'resource_id': 100},
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(resource.downvotes()), 1)

    def test_user_can_get_persisten_vote(self):
        self.assertTrue(self.login)
        resource = self.create_resources()
        response = self.client.post('/resource/100/unlike', {'resource_id': 100},
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        response = self.client.post('/resource/100/like', {'resource_id': 100},
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(resource.upvotes()), 1)

    def test_user_cannot_vote_more_than_once(self):
        self.assertTrue(self.login)
        resource = self.create_resources()
        response = self.client.post('/resource/100/unlike', {'resource_id': 100},
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        response = self.client.post('/resource/100/unlike', {'resource_id': 100},
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(resource.upvotes()), 0)
