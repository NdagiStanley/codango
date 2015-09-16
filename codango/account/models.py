from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User

# Create your models here.


class UserProfile(models.Model):
    def get_short_name(self):
        pass

    def get_full_name(self):
        pass

    user = models.OneToOneField(User)
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

