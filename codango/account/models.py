from bootstrapform import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User
from django.db.models.signals import post_save

# Create your models here.


class UserProfile(models.Model):
    def get_short_name(self):
        pass

    def get_full_name(self):
        pass

    user = models.OneToOneField(User)
    place_of_work = models.CharField(max_length=150, blank=True)
    position = models.CharField(max_length=10, blank=True)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)

    # photo = models.FileField()

    # username = models.CharField(max_length=100, unique=True)
    # first_name = models.CharField(max_length=150)
    # last_name = models.CharField(max_length=150)

# User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
