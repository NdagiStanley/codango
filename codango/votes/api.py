from rest_framework import generics
from serializers import VoteSerializer
from models import Vote


class VoteListAPIView(generics.ListCreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

class VoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
