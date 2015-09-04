from django.test import TestCase
from resources import views
from django.test import Client
from resources.models import Resource
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

class ResourceTestViews(TestCase):

	def setUp(self): 
		self.client = Client()   

	def test_ListView(self):
		url = reverse("resources.views.ListView")
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertIn(create.title, response.content)