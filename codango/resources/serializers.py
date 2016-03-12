from rest_framework import serializers

from models import Resource
from comments.serializers import CommentSerializer


class ResourceSerializer(serializers.ModelSerializer):
    """Resource Serializer"""

    comments = CommentSerializer(many=True)
    author = serializers.ReadOnlyField(source='user.username')


    class Meta:
        model = Resource
        fields = ('author', 'text', 'language_tags', 'resource_file',
                  'resource_file_name', 'resource_file_size', 'snippet_text',
                  'date_added', 'date_modified', 'comments')

        read_only_fields = ('date_modified', 'date_added')
