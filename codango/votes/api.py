from rest_framework import generics
from serializers import VoteSerializer
from models import Vote


class VoteListAPIView(generics.ListCreateAPIView):
    """For /api/v1/votes/ url path"""
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

class VoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """For /api/v1/votes/ url path"""
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
