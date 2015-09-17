from django.test import TestCase, Client, RequestFactory
from resources import views
from resources.models import Resource
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from resources.views import ResourceCreate
from resources import forms
import unittest


class ResourceCreateTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='inioluwa', email='fagemaki.iniruto@yahoo.com', password='iniruto')

    def test_get(self):
        # Creating an instance of a GET request.
        request = self.factory.get('create')

        # Instatiating view
        view = ResourceCreate.as_view(template_name='create.html')
        response = view(request)

        # Testing
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'create.html')
        self.assertEqual(response.context_data['form'], ResourceForm)

    def test_post(self):
        pass
