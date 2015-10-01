from django.forms import ModelForm
from .models import Resource

class ResourceForm(ModelForm):

    class Meta:
        model = Resource
        fields = ['text', 'resource_file', 'language_tags']

    def __init__(self, *args, **kwargs):
        super(ResourceForm, self).__init__(*args, **kwargs)
        self.fields['text'].required = False
        self.fields['resource_file'].required = False
        self.fields['language_tags'].required = False
