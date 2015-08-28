#import unittest
from django.test import TestCase
#from resources import models
from resources.models import Resources

class ModelsTestCase(TestCase):

	def test_resource_text(self):
		self.assertEqual(resource_text, models.CharField(max_length=1024))

	# def test_check(self):
	# 	self.assertEqual(1+3, 4)
