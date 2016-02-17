from rest_framework import viewsets

from resources.models import Resource
from api.serializers.resources_serializers import ResourceSerializer


class ResourceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
