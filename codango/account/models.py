from uuid import uuid4
from bootstrapform import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField

# Create your models here.


def get_upload_file_name(instance, filename):
    # path = "upload/path/"
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        # filename = '{}.{}'.format(uuid4().hex, ext)
        filename = instance.userid + instance.file_extension
        # return the whole path to the file
        # return os.path.join(path, filename)
    print filename
    # return 'uploads/%s' % filename
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

    photo = models.FileField(upload_to=get_upload_file_name, blank=True)

    image = CloudinaryField('image', default="image/upload/v1443782603/vqr7n59zfxyeybttleug.gif")
    # full_name = models.CharField(max_length=100)


    # username = models.CharField(max_length=100, unique=True)
    # first_name = models.CharField(max_length=150)
    # last_name = models.CharField(max_length=150)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
