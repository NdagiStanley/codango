from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Session(models.Model):
    session_name = models.CharField(max_length=200, null=True)
    last_active_date = models.DateTimeField(default=timezone.now())
    status = models.BooleanField(default=True)
    initiator = models.ForeignKey(User)


class Participant(models.Model):
    participant = models.ForeignKey(User)
    session_id = models.ForeignKey(Session)
    joined_date = models.DateTimeField(default=timezone.now())
