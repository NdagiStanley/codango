from rest_framework import generics, permissions
from serializers import ResourceSerializer
from models import Resource


class ResourceListAPIView(generics.ListCreateAPIView):
    """For /api/v1/resources/ url path."""

    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer


class ResourceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """For /api/v1/resources/<resource_id> url path."""

    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
