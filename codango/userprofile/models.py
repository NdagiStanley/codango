from bootstrapform import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import register

# Create your models here.


class UserProfile(models.Model):

    user = models.OneToOneField(User)
    social_id = models.CharField(max_length=200, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    place_of_work = models.CharField(max_length=150, blank=True)
    position = models.CharField(max_length=100, blank=True)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    about = models.TextField(max_length=1200,blank=True)
    github_username = models.CharField(max_length=200, null=True)

    image = CloudinaryField(
        'image', default="image/upload/v1443782603/vqr7n59zfxyeybttleug.gif")

    def get_user(self):
        return User.objects.get(id=self.user_id)

    def get_followers(self):
        followers = Follow.objects.filter(followed=self.user_id)
        return followers

    def get_following(self):
        following = Follow.objects.filter(follower=self.user_id)
        return following


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)


class Follow(models.Model):

    follower = models.ForeignKey(User, related_name='follower')
    followed = models.ForeignKey(User, related_name='following')
    date_of_follow = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('follower', 'followed'),)



class Language(models.Model):

    user = models.ForeignKey(User,related_name="languages")
    name = models.CharField(max_length=200, null=True)

    class Meta:
        unique_together = (('user', 'name'),)

    def __str__(self):
        return self.name

class Notifications(models.Model):

    user = models.ForeignKey(User,related_name="notifications")
    link = models.CharField(max_length=200, null=True)
    activity_type = models.CharField(max_length=50, null=False)
    read = models.BooleanField()
    content = models.TextField(max_length=1200,blank=False)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

