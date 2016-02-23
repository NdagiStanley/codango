from rest_framework import serializers
from pairprogram.models import Session, Participant

class SessionSerializer(serializers.ModelSerializer):
    """
    Session Serializer
    """
    class Meta:
        model = Session
        fields = ('session_name', 'last_active_date', 'status', 'initiator')

class ParticipantSerializer(serializers.ModelSerializer):
    """
    Participant serializer
    """
    class Meta:
        model = Participant
        fields = ('participant', 'session', 'joined_date')
