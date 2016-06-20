from rest_framework import generics, permissions
from serializers import ResourceSerializer, ResourceVoteSerializer
from models import Resource
from votes.models import Vote


class ResourceListAPIView(generics.ListCreateAPIView):

    """For /api/v1/resources/ url path."""

    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

    def perform_create(self, serializer):
        """Associate resource to an account,save data passed in request."""
        serializer.save(author=self.request.user)


class ResourceVotesAPIView(generics.ListCreateAPIView):

    """For /api/v1/resources/<resource_id>/votes/ url path."""

    #queryset = Vote.objects.all()
    serializer_class = ResourceVoteSerializer

    def perform_create(self, serializer):
        """Associate resource to an account,save data passed in request."""
        resource = Resource.objects.filter(id=self.kwargs.get('pk', 0)).first()
        serializer.save(user=self.request.user, resource=resource)

    def get_queryset(self):
        resource = Resource.objects.filter(id=self.kwargs.get('pk', 0))
        return Vote.objects.filter(resource=resource)


class ResourceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):

    """For /api/v1/resources/<resource_id> url path."""

    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
