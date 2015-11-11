from django.db import models
from django.contrib import auth
from resources.models import Resource


class Comment(models.Model):
	author = models.ForeignKey(auth.models.User)
	resource = models.ForeignKey(Resource)
	content = models.TextField(null=False, blank=False)
	date_created = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.content
