import unittest
from django.test import TestCase
from resources import views

def test_resources_views():
	create = self.create_resource()
	url = reverse("resources.views.resources")

	self.assertEqual(resp.status_code, 200)
	self.assertIn(create.title, resp.content)