from django.forms import ModelForm
from .models import Resource, Snippet
from django_ace import AceWidget


class ResourceForm(ModelForm):

    class Meta:
        model = Resource
        fields = ['text', 'resource_file', 'language_tags']

    def __init__(self, *args, **kwargs):
        super(ResourceForm, self).__init__(*args, **kwargs)
        self.fields['text'].required = False
        self.fields['resource_file'].required = False
        self.fields['language_tags'].required = False


class SnippetForm(ModelForm):

    class Meta:
        model = Snippet
        fields = ['text']
        widgets = {
            'text': AceWidget(theme='twilight'),
        }

    def clean_text(self):
        value = self.cleaned_data['text']
        if 'valid' not in value:
            raise ValidationError("Must contain the string 'valid'")
        return value
