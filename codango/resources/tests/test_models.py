from django.test import TestCase
from resources.models import Resource
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class ResourceTestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='inioluwafageyinbo', password='codango')

    def create_resources(self, text='some more words', resource_file='resource_file'):
        return Resource.objects.create(text=text, author=self.user, resource_file=resource_file)

    def test_for_resource_creation(self):
        create = self.create_resources()
        self.assertTrue(isinstance(create, Resource))
