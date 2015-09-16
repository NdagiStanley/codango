from django.forms import ModelForm
from .models import Resource


class ResourceForm(ModelForm):

    class Meta:
        model = Resource
        fields = ['title', 'text', 'resource_type', 'resource_file']
