from rest_framework import serializers
from votes.models import Vote

class VoteSerializer(serializers.ModelSerializer):
    """
    Vote Serializer
    """
    class Meta:
        model = Vote
        fields = ('user', 'resource', 'vote', 'time_stamp')
