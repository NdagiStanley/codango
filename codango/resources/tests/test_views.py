from django.test import TestCase, Client, RequestFactory
from resources import views
from resources.models import Resource
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from resources.views import ResourceCreate, ResourceList, ResourceDetail
from resources.forms import ResourceForm
import unittest


class ResourceViewsTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='inioluwa', email='fagemaki.iniruto@yahoo.com', password='iniruto')

    def test_create_get(self):
        # Creating an instance of a GET request.
        request = self.factory.get('create')

        # Instatiating view
        view = ResourceCreate.as_view(template_name='create.html')
        response = view(request)

        # Testing
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'create.html')
        self.assertIsInstance(response.context_data['form'], ResourceForm)

    def test_create_post(self):
        pass

    def test_list_get(self):
        request = self.factory.get('list')

        view = ResourceList.as_view()
        response = view(request)
        resource_list = Resource.objects.all()

        self.assertEqual(resource_list, resource_list)
        self.assertEqual(response.template_name[1], 'list.html')
        self.assertIsInstance(resource_list, 'list.html')

    def test_detail_get(self):
        pass
