from django.contrib.auth import logout
from django.contrib import messages
from django.utils import timezone
from django.shortcuts import redirect

from codango.settings import base

class SessionIdleTimeout:
    def process_request(self, request):
        if request.user.is_authenticated():
            current_datetime = timezone.now()
            last_action = request.user.userprofile.last_action
            last = (current_datetime - last_action).seconds
            if last > base.SESSION_IDLE_TIMEOUT:
                logout(request)
            else:
                request.user.userprofile.last_action = current_datetime
                request.user.userprofile.save()
        return None
