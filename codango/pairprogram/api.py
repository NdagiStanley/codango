from rest_framework import generics
from serializers import ParticipantSerializer, SessionSerializer
from models import Participant, Session


class SessionListAPIView(generics.ListCreateAPIView):
    """For /api/v1/pairprogram/sessions/ url path."""

    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class SessionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """For /api/v1/pairprogram/sessions/<session_id> url path."""

    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class ParticipantListAPIView(generics.ListCreateAPIView):
    """For /api/v1/pairprogram/sessions/<session_id>/participants/ path."""

    serializer_class = ParticipantSerializer

    def get_queryset(self):
        """Retrieve only a particular sessions's participants."""
        session_id = self.kwargs['pk']
        participant = Participant.objects.filter(session=session_id)
        return participant


class ParticipantDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """/api/v1/pairprogram/sessions/<session_id>/participant/
       <participant_id>/  path.
    """

    serializer_class = ParticipantSerializer

    def get_queryset(self):
        """Retrieve specific participant from a session."""
        session_id = self.kwargs['session_id']
        participant = Participant.objects.filter(session=session_id)
        return participant
