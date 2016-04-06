from bootstrapform import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import register


class UserProfile(models.Model):

    user = models.OneToOneField(User)
    social_id = models.CharField(max_length=200, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    place_of_work = models.CharField(max_length=150, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    about = models.TextField(max_length=1200, null=True, blank=True)
    github_username = models.CharField(max_length=200, null=True)
    frequency = models.CharField(max_length=200, default='none')

    image = CloudinaryField(
        'image', default="image/upload/v1443782603/vqr7n59zfxyeybttleug.gif")

    def get_user(self):
        return User.objects.get(id=self.user_id)

    def get_followers(self):
        followers = self.user.follower.all()
        return [follower for follower in followers]

    def get_following(self):
        followings = self.user.following.all()
        return [following for following in followings]

    @property
    def followings(self):
        followers = self.user.follower.all()
        follow = []
        for follower in followers:
            follow.append(
                {'id': follower.followed.id,
                 'following': follower.followed.username,
                 'follow_date': follower.date_of_follow})
        return follow

    @property
    def followers(self):
        followings = self.user.following.all()
        follow = []
        for following in followings:
            follow.append(
                {'id': following.follower.id,
                 'follower': following.follower.username,
                 'follow_date': following.date_of_follow})
        return follow

    @property
    def languages(self):
        return [language for language in self.user.languages.all()]


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)


class UserSettings(models.Model):

    user = models.ForeignKey(User, related_name='settings')
    frequency = models.CharField(default="daily", null=True, max_length=10)

    @property
    def languages(self):
        return [language for language in self.user.languages.all()]


class Follow(models.Model):

    follower = models.ForeignKey(User, related_name='follower')
    followed = models.ForeignKey(User, related_name='following')
    date_of_follow = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('follower', 'followed'),)


class Language(models.Model):

    user = models.ForeignKey(User, related_name="languages")
    name = models.CharField(max_length=200, null=True)

    class Meta:
        unique_together = (('user', 'name'),)

    def __str__(self):
        return self.name


class Notification(models.Model):

    user = models.ForeignKey(User, related_name="notifications")
    link = models.CharField(max_length=200, null=True)
    activity_type = models.CharField(max_length=50, null=False)
    read = models.BooleanField()
    content = models.TextField(max_length=1200, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-date_created']
