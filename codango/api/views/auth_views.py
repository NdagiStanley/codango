from django.contrib.auth.models import User

from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token


from api import serializers

# Default permission_classes = (permissions.IsAuthenticated,)

class UserRegister(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserLogOut(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
