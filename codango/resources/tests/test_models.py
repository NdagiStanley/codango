from django.test import TestCase
from resources.models import Resource
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class ResourceTestModels(TestCase):

	def setUp(self):
		self.user = User.objects.create(username='inioluwafageyinbo', password='codango')

	def create_resources(self, title = "Some words", text = "some more words"):
		return Resource.objects.create(title = title, text = text, author = self.user)

	def test_for_resource_creation(self):
		create = self.create_resources()
		self.assertTrue(isinstance(create, Resource))
		self.assertEqual(create.__str__(), create.title)