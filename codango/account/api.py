from rest_framework import generics, permissions
from serializers import UserSerializer
from django.contrib.auth.models import User


class UserRegisterAPIView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserLogoutAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
