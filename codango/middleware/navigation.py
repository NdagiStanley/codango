
class NavigationMiddleWare(object):
    """
    Middle ware that handles page tab highlight on navigation response for every request
    """

    def process_template_response(self, request, response):
        """
        Middleware hook method called immediately after the
        view function returns a response.
        """
        active_tab = request.path.strip('/')
        if not response.context_data:
            response.context_data = {}
        if isinstance(response.context_data, dict):
            response.context_data.update({
                'active_tab': active_tab
            })
        return response
