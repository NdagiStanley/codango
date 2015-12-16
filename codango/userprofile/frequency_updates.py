from userprofile.models import UserProfile
from django.contrib.auth.models import User


def daily_updates():
    users = UserProfile.objects.filter(frequency='daily')
    userids = [user.user_id for user in users]
    emails = [User.objects.get(id=userid).email for userid in userids]
    return emails


def weekly_updates():
    users = UserProfile.objects.filter(frequency='weekly')
    userids = [user.user_id for user in users]
    emails = [User.objects.get(id=userid).email for userid in userids]
    return emails


def monthly_updates():
    users = UserProfile.objects.filter(frequency='monthly')
    userids = [user.user_id for user in users]
    emails = [User.objects.get(id=userid).email for userid in userids]
    return emails
