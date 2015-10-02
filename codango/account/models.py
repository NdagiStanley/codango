from uuid import uuid4
from bootstrapform import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField

# Create your models here.


def get_upload_file_name(instance, filename):

    ext = filename.split('.')[-1]

    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:

        filename = instance.userid + instance.file_extension

    print filename
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class UserProfile(models.Model):
    def get_short_name(self):
        pass

    def get_full_name(self):
        pass

    user = models.OneToOneField(User)
    place_of_work = models.CharField(max_length=150, blank=True)
    position = models.CharField(max_length=100, blank=True)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)

    image = CloudinaryField('image', default="image/upload/v1443782603/vqr7n59zfxyeybttleug.gif")


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
