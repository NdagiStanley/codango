from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from pairprogram.models import Session, Participant
from api.serializers.pairprogram_serializers import SessionSerializer, ParticipantSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def sessions_list(request):
    """
    List all sessions in pair programming
    """
    if request.method == 'GET':
        sessions = Session.objects.all()
        serializer = SessionSerializer(sessions, many=True)
        return JSONResponse(serializer.data)

@csrf_exempt
def participants_list(request):
    """
    List all participants in pair programming sessions
    """
    if request.method == 'GET':
        participants = Participant.objects.all()
        serializer = ParticipantSerializer(participants, many=True)
        return JSONResponse(serializer.data)
