"""Middleware class to handle retrieval of popular resources."""
from django.db.models import Count
from resources.models import Resource


class PopularResourcesMiddleware(object):
    """Middle ware to handle popular resources response for every request."""

    def process_template_response(self, request, response):
        """Hook to call middleware each time a response is made."""
        if not response.context_data:
            response.context_data = {}
        if request.user.is_authenticated():
            response.context_data.update({
                'popular': Resource.objects.annotate(
                    num_comments=Count('comments')).annotate(
                    num_votes=Count('votes')).order_by(
                    '-num_comments', '-num_votes')[:5]
            })
        return response
