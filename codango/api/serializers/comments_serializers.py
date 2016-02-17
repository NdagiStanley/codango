from rest_framework import serializers
from comments.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    """
    Comment Serializer
    """
    class Meta:
        model = Comment
        fields = ('author', 'resource', 'content', 'date_created', 'date_modified')
