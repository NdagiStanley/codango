from rest_framework import generics, permissions
from serializers import CommentSerializer
from models import Comment


class CommentListAPIView(generics.ListCreateAPIView):
    """For /api/v1/comments/ url path"""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """For /api/v1/comments/<comments_id> url path"""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
