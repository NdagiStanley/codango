from rest_framework import serializers

from models import Resource
from votes.models import Vote
from comments.serializers import CommentSerializer


class ResourceSerializer(serializers.ModelSerializer):
    """Resource Serializer"""

    comments = CommentSerializer(many=True, read_only=True)
    author = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Resource
        fields = ('id', 'author', 'text', 'language_tags', 'resource_file',
                  'resource_file_name', 'resource_file_size', 'snippet_text',
                  'date_added', 'date_modified', 'comments')

        read_only_fields = ('date_modified', 'date_added', 'comments')


class ResourceVoteSerializer(serializers.ModelSerializer):
    """Resource Votes Serializer"""

    user = serializers.ReadOnlyField(source='user.username')
    resource = serializers.ReadOnlyField(source='resource.text')

    class Meta:
        model = Vote
        fields = ('id', 'user', 'vote', 'resource', 'time_stamp')

        read_only_fields = ('time_stamp')
