from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import pre_delete
from django.dispatch import receiver

class Session(models.Model):
    session_name = models.CharField(max_length=200, null=True)
    last_active_date = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=True)
    initiator = models.ForeignKey(User)


class Participant(models.Model):
    participant = models.ForeignKey(User)
    session = models.ForeignKey(Session)
    joined_date = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = (('participant', 'session'),)

@receiver(pre_delete, sender=Session)
def delete_related_participants(sender, instance, **kwargs):
    Participant.objects.filter(session=instance.id).delete()
