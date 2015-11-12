from django.db import models
from django.contrib import auth
from django.core.urlresolvers import reverse
from cloudinary.models import CloudinaryField


class Resource(models.Model):

    LANGUAGE_TAGS = (
        ('PYTHON', 'Python'),
        ('RUBY', 'Ruby'),
        ('ANDROID', 'Android'),
        ('MARKUP', 'HTML/CSS'),
        ('JAVA', 'Java'),
        ('PHP', 'PHP'),
        ('IOS', 'IOS'),
        ('JS', 'Javascript'),
        ('C', 'C')
    )

    author = models.ForeignKey(auth.models.User)
    text = models.TextField(null=True, blank=False)
    language_tags = models.CharField(
        max_length=30, choices=LANGUAGE_TAGS, default='Untagged')
    resource_file = CloudinaryField(
        'resource_file', null=True, blank=True)
    resource_file_name = models.CharField(max_length=100, null=True)
    resource_file_size = models.IntegerField(default=0)
    snippet_text = models.TextField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])


    def upvotes(self):
        liked_ids = [vote.user.id for vote in self.votes.all() if vote.vote is True]

        return liked_ids
    def downvotes(self):
        unliked_ids = [vote.user.id for vote in self.votes.all() if vote.vote is False]

        return unliked_ids

