from rest_framework import viewsets

from votes.models import Vote
from api.serializers.votes_serializers import VoteSerializer


class VoteViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
