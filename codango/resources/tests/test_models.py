from django.test import TestCase
from resources.models import Resource
from django.contrib.auth.models import User
from django.test.client import Client
from django.core.urlresolvers import reverse

class ResourceTest(TestCase):

	# def setUp(self):
	# 	self.client = client()
		#person = self.client.session['_auth_user_id']

	def test_for_resources(self, title = "Some words", text = "some more words", author = '_auth_user_id'):
		return Resource.objects.create(title = title, text = text, author = author)

	def test_for_resource_creation(self):
		create = self.create_resources()
		self.assertTrue(isinstance(create, Resource))
		self.assertEqual(create.__str__(), create.title)