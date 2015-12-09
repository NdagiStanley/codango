from django.forms import ModelForm
from models import Resource
from cloudinary.forms import CloudinaryFileField


class ResourceForm(ModelForm):

    class Meta:
        model = Resource
        fields = ['text', 'resource_file', 'language_tags', 'snippet_text']

    resource_file = CloudinaryFileField(
        required=False,
        options={
            'resource_type': 'raw',
            'use_filename': True,
            'allowed_formats': ['pdf', 'doc', 'docx']
        })

    def __init__(self, *args, **kwargs):
        super(ResourceForm, self).__init__(*args, **kwargs)
        self.fields['text'].required = True
        self.fields['language_tags'].required = False
        self.fields['snippet_text'].required = False
