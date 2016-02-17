from rest_framework import viewsets

from pairprogram.models import Session, Participant
from api.serializers.pairprogram_serializers import SessionSerializer, ParticipantSerializer


class SessionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class ParticipantViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
