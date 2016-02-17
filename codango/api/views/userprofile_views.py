from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from userprofile.models import UserProfile, Follow, Language, Notification
from api.serializers.userprofile_serializers import UserProfileSerializer, FollowSerializer, NotificationSerializer, LanguageSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def userprofile_list(request):
    """
    List all profiles of users
    """
    if request.method == 'GET':
        userprofiles = UserProfile.objects.all()
        serializer = UserProfileSerializer(userprofiles, many=True)
        return JSONResponse(serializer.data)

@csrf_exempt
def follow_list(request):
    """
    List all follows on users profiles
    """
    if request.method == 'GET':
        follows = Follow.objects.all()
        serializer = FollowSerializer(follows, many=True)
        return JSONResponse(serializer.data)

@csrf_exempt
def language_list(request):
    """
    List all languages on users profiles
    """
    if request.method == 'GET':
        languages = Language.objects.all()
        serializer = LanguageSerializer(languages, many=True)
        return JSONResponse(serializer.data)


@csrf_exempt
def notification_list(request):
    """
    List all notifications on users profiles
    """
    if request.method == 'GET':
        notifications = Notification.objects.all()
        serializer = NotificationSerializer(notifications, many=True)
        return JSONResponse(serializer.data)
