from rest_framework import generics
from serializers import CommentSerializer
from models import Comment


class CommentListAPIView(generics.ListCreateAPIView):
    """For /api/v1/resources/<resource_id>/comments/ url path."""

    serializer_class = CommentSerializer

    def get_queryset(self):
        """Return comments belonging to resource specified on URL."""
        resource_id = self.kwargs['pk']
        return Comment.objects.filter(resource=resource_id)


class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """For /api/v1/resources/<resource_id>/comments/<comments_id> url path."""

    serializer_class = CommentSerializer

    def get_queryset(self):
        """Return comment specified on URL."""
        resource_id = self.kwargs['resource_id']
        comments = Comment.objects.filter(resource=resource_id)
        return comments
