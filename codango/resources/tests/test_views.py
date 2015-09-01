from django.test import TestCase
from resources import views
from django.test import Client
from resources.models import Resource
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

class ResourceTestViews(TestCase):

	def setUp(self): 
		cli = Client()   
		#response = cli.post('/login', {'username': 'inioluwa', 'password': 'codango'})

	def test_ListView(self):
		url = reverse("resources.views.ListView")
		resp = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertIn(create.title, resp.content)
		

	# def test_ListView(self):
	# 	Resource.objects.create()
	# 	view = ListView.as_view()
	# 	response = view()
	# 	self.assertEqual(response.status_code, 200)
	# 	self.assertIn(create.title, response.content)


	# def test_resources_views():
	# 	# create = self.create_resource()
	# 	url = reverse("resources.views.resources")

	# 	self.assertEqual(resp.status_code, 200)
	# 	self.assertIn(create.title, resp.content)

	# def create_resources(self, title = "Some words", text = "some more words"):
	# 	return Resource.objects.create(title = title, text = text, author = self.client)

	# def test_ListView(self):
	# 	c = self.create_resources()
	# 	url = reverse("resources.views.resources")
	# 	response = self.client.get(url)
	# 	self.assertEqual(response.status_code, 200)
	# 	self.assertIn(c.title, response.content)