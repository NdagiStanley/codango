from django.db import models
from django.contrib import auth
from django.core.urlresolvers import reverse
import datetime
# Create your models here.


class Resource(models.Model):

    RESOURCE_TYPES = (
        ('PDF', 'PDF Document'),
        ('CODE', 'Code Snippet'),
        ('LINK', 'Resource URL'),
        ('IMAGE', 'Image file'),
        ('VIDEO', 'Video file')
    )
    author = models.ForeignKey(auth.models.User)
    text = models.TextField(null=True, blank=True)
    resource_type = models.CharField(
        max_length=30, choices=RESOURCE_TYPES, default='CODE')
    resource_file = models.FileField(upload_to="C:\\Users\\IniOluwa Fageyinbo\\Documents\\projects\\codango\\codango", null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
