from rest_framework import serializers
from resources.models import Resource

class ResourceSerializer(serializers.ModelSerializer):
    """
    Resource Serializer
    """
    class Meta:
        model = Resource
        fields = ('author', 'text', 'language_tags', 'resource_file', 'resource_file_name', 'resource_file_size', 'snippet_text', 'date_added', 'date_modified')
