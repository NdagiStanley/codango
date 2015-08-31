from django.db import models
from django.contrib import auth
from django.core.urlresolvers import reverse

# Create your models here.

class Resource(models.Model):
	author = models.ForeignKey(auth.models.User)
	title = models.CharField(max_length=200)
	text = models.TextField()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('resources_detail', args=[str(self.id)])