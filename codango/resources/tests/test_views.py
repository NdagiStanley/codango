from django.test import TestCase, Client
from resources import views
from resources.models import Resource
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse, resolve
from django.contrib.auth.models import User
from resources.views import ResourceCreate, ResourceList, ResourceDetail, ResourceUpdate
from resources.forms import ResourceForm
from resources.models import Resource
import unittest


class ResourceCreateViewTest(TestCase):

    def test_get_returns_resource_form_in_template(self):
        response = self.client.get('/resources/create/')

        self.assertIsInstance(response.context['form'], ResourceForm)
        self.assertEqual(response.status_code, 200)

    # def test_post_creates_new_resource(self):
    #     response = self.client.post('resources/create')

    # def test_post_redirects_to_resources_list(self):
    #     response = self.client.post('/resources/create/')


class ResourceListViewTest(TestCase):

    def test_get_returns_resource_list(self):
        response = self.client.get('/resources/list/')

        self.assertEqual(response.status_code, 200)


class ResourceDetailViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User(username='ini')
        self.user.set_password('blah')
        self.user.save()
        self.test_resource = Resource(
            author=self.user, title='A title', text='some text')
        self.test_resource.save()

    def test_get_returns_resource_detail(self):
        pk = self.test_resource.pk
        self.test_resource_detail = Resource.objects.get(id=pk)
        response = self.client.get(
            reverse('resources_detail', kwargs={'pk': pk}))

        self.assertTrue(
            response, self.test_resource_detail)
        self.assertEqual(response.status_code, 200)


class ResourceUpdateViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User(username='ini')
        self.user.set_password('blah')
        self.user.save()
        self.test_resource = Resource(
            author=self.user, title='A title', text='some text')
        self.test_resource.save()

    def test_get_returns_resource_form_with_form_data(self):
        pk = self.test_resource.pk
        response = self.client.get(
            reverse('resources_update', kwargs={'pk': pk}))

        self.assertIsInstance(response.context['resource_form'], ResourceForm)
        self.assertEqual(response.status_code, 200)
