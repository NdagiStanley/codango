from django.forms import ModelForm
from .models import Resource


class ResourceTextForm(ModelForm):

    class Meta:
        model = Resource
        fields = ['author', 'title', 'text', 'resource_type']


class ResourcePDFForm(ModelForm):

    class Meta:
        model = Resource
        fields = ['author', 'title', 'resource_file', 'resource_type']
