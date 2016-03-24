from rest_framework import generics
from serializers import ParticipantSerializer, SessionSerializer
from models import Participant, Session


class SessionListAPIView(generics.ListCreateAPIView):
    """Handle the URL to create a session and list all sessions.

    URL : /api/v1/pairprogram/sessions/
    Args:
        To create a session:
            session_name -- the required session name
            initiatior -- creator of the session
    Returns:
        Dictionary containing session details inclusive of session id, name,
            participants, initiator and last active date.
    """

    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class SessionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Handle the URL to list, edit or delete a specific session.

    URL : /api/v1/pairprogram/sessions/<session_id>
    Args:
        To get or delete the session:
            pk -- the session id lookup field from the URL
        To edit the session details:
           param1(int)-pk -- session id lookup field from the URL
           param2 (optional) - session name
    Returns:
        PUT/GET -- Dictionary containing session details inclusive of
                session id, name,participants, initiator and last active date.
        DELETE -- 204 status code
    """

    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class ParticipantListAPIView(generics.ListCreateAPIView):
    """Handle the URL to view all participants or add a participant to a session.

    URL : /api/v1/pairprogram/sessions/<session_id>/participants
    Args:
        To get the participants
            session id -- the session id lookup field picked from the URL
        To add a participant to the sesion
           param1(int)-session id -- the session id lookup field from the URL
           param2(int) - participants user id
    Returns:
        Dictionary containing participant's details inclusive of session name,
            participant's id and last active date.
    """

    serializer_class = ParticipantSerializer
    lookup_field = ('session_id')

    def get_queryset(self):
        """Retrieve only a particular sessions's participants."""
        session_id = self.kwargs['session_id']
        participant = Participant.objects.filter(session=session_id)
        return participant


class ParticipantDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Handle the URL to list, edit or delete a specific session.

    URL :/api/v1/pairprogram/sessions/<session_id>/participant/<participant_id>
    Args:
        To get or delete a specific participant from the session:
            session_id -- the session id lookup field from the URL
            id -- participant id
        To edit the participant's details:
           param1(int)-session id -- session id lookup field from the URL
           param1(int)-participant id-- participantid lookup field from the URL
    Returns:
        PUT/GET -- Dictionary containing participant's details inclusive of
                session name, participant's id and last active date.
        DELETE -- 204 status code
    """

    serializer_class = ParticipantSerializer
    lookup_field = ('id')

    def get_queryset(self):
        """Retrieve specific participant from a session."""
        session_id = self.kwargs['session_id']
        participant = Participant.objects.filter(
            session=session_id)
        return participant
