from django.forms import ModelForm
from models import Resource

class ResourceForm(ModelForm):

    class Meta:
        model = Resource
        fields = ['text', 'resource_file', 'language_tags', 'snippet_text']

    def __init__(self, *args, **kwargs):
        super(ResourceForm, self).__init__(*args, **kwargs)
        self.fields['text'].required = False
        self.fields['resource_file'].required = False
        self.fields['language_tags'].required = False
        self.fields['snippet_text'].required = False
