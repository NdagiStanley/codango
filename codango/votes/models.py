from django.db import models
from django.contrib import auth
from resources.models import Resource


class Vote(models.Model):
	user = models.ForeignKey(auth.models.User)
	resource = models.ForeignKey(Resource,related_name="votes")
	vote = models.BooleanField()
	time_stamp = models.DateTimeField(editable=False, auto_now=True)

	class Meta:
		unique_together = (('user', 'resource', 'vote'),)

	def __str__(self):
		return '%s: %s on %s' % (self.user, self.vote, self.object)

	def is_upvote(self):
		return self.vote is True

	def is_downvote(self):
		return self.vote is not True
