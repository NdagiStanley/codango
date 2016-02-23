from rest_framework import viewsets

from comments.models import Comment
from api.serializers.comments_serializers import CommentSerializer


class CommentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
