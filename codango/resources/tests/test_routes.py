from django.test import TestCase, Client
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse, resolve
from django.contrib.auth.models import User
from resources.views import ResourceCreate, ResourceList, ResourceDetail, ResourceUpdate
from resources.forms import ResourceTextForm, ResourcePDFForm
from resources.models import Resource


class ResourceCreateViewTest(TestCase):

    def test_get_returns_resource_form_in_template(self):
        response = self.client.get('/resources/create/')

        self.assertIsInstance(response.context['form'], ResourceForm)
        self.assertEqual(response.status_code, 200)

    def test_post_creates_new_text_resource(self):
        response = self.client.post('/resources/create/', {
            'author': 'lade.o',
            'title': 'lade-git',
            'text': 'lade-git is vast in git',
            'resource_type': 'CODE'
        })

        self.assertEquals(response.status_code, 302)

    def test_post_creates_new_pdf_resource(self):
        response = self.client.post('/resources/create/', {
            'author': 'lade.o',
            'title': 'lade-git',
            'resource_type': 'PDF'
        })

        self.assertEquals(response.status_code, 302)


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
