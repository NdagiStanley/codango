from django.db import models
from django.contrib import auth
from django.core.urlresolvers import reverse

# Create your models here.

class Resource(models.Model):
	author = models.ForeignKey(auth.models.User)
	text = models.TextField(max_length=1024)

	def get_absolute_url(self):
		return reverse('resources_detail', args=[str(self.id)])