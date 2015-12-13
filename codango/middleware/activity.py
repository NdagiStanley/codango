from userprofile.models import Notification


class ActivityMiddleWare(object):
    """
    Middle ware that handles activities response for every request
    """

    def process_template_response(self, request, response):
        """
        Middleware hook method called immediately after the
        view function returns a response.
        """
        if request.user.is_authenticated():
            response.context_data.update({
                'unread': request.user.notifications.all().filter(read=False),
                'activites': request.user.notifications.all(),
                })
        return response