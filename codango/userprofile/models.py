from bootstrapform import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import register

# Create your models here.


class UserProfile(models.Model):

    user = models.OneToOneField(User)
    fb_id = models.CharField(max_length=200, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    place_of_work = models.CharField(max_length=150, blank=True)
    position = models.CharField(max_length=100, blank=True)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    about = models.TextField(max_length=1200,blank=True)

    image = CloudinaryField(
        'image', default="image/upload/v1443782603/vqr7n59zfxyeybttleug.gif")

    def get_user(self):
        return User.objects.get(id=self.user_id)

    def get_followers(self):
        followers = Follow.objects.filter(follower_id=self.user_id)
        return followers

    def get_following(self):
        following = Follow.objects.filter(followed_id=self.user_id)
        return following

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)


class Follow(models.Model):

    follower_id = models.ForeignKey(User, related_name='follower')
    followed_id = models.ForeignKey(User, related_name='following')
    date_of_follow = models.DateTimeField(auto_now_add=True)

    @register.filter
    def is_following(self, id):
        followed_id = Follow.objects.get(followed_id=id)
        if followed_id:
            return True
        else:
            return False
