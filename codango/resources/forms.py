from django.forms import ModelForm
from .models import Resource

class ResourceForm(ModelForm):

    class Meta:
        model = Resource
        fields = ['author', 'title', 'text', 'resource_type', 'resource_file']

# class ResourceForm(ModelForm):

#     class Meta:
#         model = Resource
#         fields = ['author', 'title', 'resource_type']


# class PDFForm(ResourceForm):

#     class Meta:
#         fields = ['resource_file']


# class CodeSnippetForm(ResourceForm):

#     class Meta:
#         fields = ['text']


# class LinkForm(ResourceForm):

#     class Meta:
#         fields = ['link']


# class ImageForm(ResourceForm):

#     class Meta:
#         fields = ['resource_file']


# class VideoForm(ResourceForm):

#     class Meta:
#         fields = ['resource_file']
