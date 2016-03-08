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

        # In respect of API
        if not response.context_data:
            response.context_data = {}
        if request.user.is_authenticated():
            response.context_data.update({
                'unread': request.user.notifications.all().filter(read=False),
                'activities': request.user.notifications.all(),
                })
        return response
