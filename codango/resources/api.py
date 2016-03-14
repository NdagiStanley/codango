from rest_framework import generics, permissions
from serializers import ResourceSerializer
from models import Resource


class ResourceListAPIView(generics.ListCreateAPIView):
    """For /api/v1/resources/ url path."""

    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

    def perform_create(self, serializer):
        """Associate resource to an account,save data passed in request."""
        serializer.save(author=self.request.user)


class ResourceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """For /api/v1/resources/<resource_id> url path."""

    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
