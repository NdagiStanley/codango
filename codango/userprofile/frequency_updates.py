from userprofile.models import UserProfile
from django.contrib.auth.models import User


def updates(frequency):
    users = UserProfile.objects.filter(frequency=frequency)
    userids = [user.user_id for user in users]
    emails = [User.objects.get(id=userid).email for userid in userids]
    return emails
