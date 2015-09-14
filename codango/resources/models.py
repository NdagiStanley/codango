from django.db import models
from django.contrib import auth
from django.core.urlresolvers import reverse
import datetime
# Create your models here.


RESOURCE_TYPES = (
    ('PDF', 'PDF Document'),
    ('CODE', 'Code Snippet'),
    ('LINK', 'Resource URL')
)


class Resource(models.Model):
    author = models.ForeignKey(auth.models.User)
    title = models.CharField(max_length=200)
    text = models.TextField()
    resource_type = models.CharField(max_length=30, choices=RESOURCE_TYPES, default='CODE')
    resource_file = models.FileField(upload_to="C:\Users\IniOluwa Fageyinbo\Documents\projects\codango\codango", null=True)
    date_added = models.DateTimeField(default=datetime.datetime.now)
    date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
