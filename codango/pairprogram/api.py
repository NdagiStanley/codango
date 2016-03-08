from rest_framework import generics
from serializers import ParticipantSerializer, SessionSerializer
from models import Participant, Session


class ParticipantListAPIView(generics.ListCreateAPIView):
    """For /api/v1/pairprogram/participants/ url path"""
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer


class ParticipantDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """For /api/v1/pairprogram/participants/<>  url path"""
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer


class SessionListAPIView(generics.ListCreateAPIView):
    """For /api/v1/pairprogram/sessions/ url path"""
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class SessionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """For /api/v1/pairprogram/sessions/<> url path"""
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
