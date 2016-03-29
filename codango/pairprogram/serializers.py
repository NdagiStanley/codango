from rest_framework import serializers

from models import Session, Participant


class ParticipantSerializer(serializers.ModelSerializer):
    """Participant serializer."""

    class Meta:
        model = Participant
        fields = ('id', 'participant', 'session', 'joined_date')

        read_only_fields = ('joined_date')


class SessionSerializer(serializers.ModelSerializer):
    """Session Serializer."""

    participants = ParticipantSerializer(many=True, read_only=True)

    class Meta:
        model = Session
        fields = ('id', 'session_name', 'last_active_date',
                  'status', 'initiator', 'participants')

        read_only_fields = ('last_active_date', 'participants')
