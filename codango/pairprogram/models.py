from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PairProgram(models.Model):

    session_id = models.CharField(max_length=100)
    session_name = models.CharField(max_length=200, null=True )
    initiator = models.ForeignKey(User, related_name='initiator', null=True)
    # participants