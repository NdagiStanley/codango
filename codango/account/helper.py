from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone


def is_user_logged_in(user_id):
    sessions = Session.objects.filter(expire_date__gte=timezone.now())

    for session in sessions:
        data = session.get_decoded()
        if(data.get('_auth_user_id', 0) == user_id):
            return True

    return False
