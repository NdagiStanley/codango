from django.db import models
from django.contrib import auth
from django.core.urlresolvers import reverse

# Create your models here.

class Resources(models.Model):
	author = models.ForeignKey(auth.models.User)
	resource_text = models.CharField(max_length=1024)

	def __str__(self):
		return self.resource_text

	def get_absolute_url(self):
		return reverse('comment_detail', args=[str(self.id)])