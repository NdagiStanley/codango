from bootstrapform import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User

# Create your models here.


class UserProfile(models.Model):
    def get_short_name(self):
        pass

    def get_full_name(self):
        pass

    user = models.OneToOneField(User)
    place_of_work = models.CharField(max_length=150)
    position = models.CharField(max_length=10)
    followers = models.IntegerField()
    following = models.IntegerField()
    # photo = models.FileField()

    # username = models.CharField(max_length=100, unique=True)
    # first_name = models.CharField(max_length=150)
    # last_name = models.CharField(max_length=150)

# User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

