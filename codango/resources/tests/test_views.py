from django.test import TestCase
from resources import views
from django.test import Client
from resources.models import Resource
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

class ResourceTestViews(TestCase):
	pass