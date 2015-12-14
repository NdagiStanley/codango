from django.test import Client,TestCase
from activity import ActivityMiddleWare
from mock import MagicMock
from django.contrib.auth.models import User
from userprofile.models import UserProfile, Follow, Notification
from django.core.urlresolvers import resolve, reverse


class ActivityMiddleWareTest(TestCase):
    """
    Testcase for the SharedContextMiddleware class
    """
    fixtures = ['initial_data.json']

    def setUp(self):
        """
        operations to run before every test
        """
        # instantiate a our middleware:
        self.activity = ActivityMiddleWare()

        # setup a mock request object and
        self.client = Client()

        # setup a mock response object and
        # add a smaple context data:
        self.request = MagicMock()
        self.response = MagicMock()
        self.response.context_data = {
            'context_var_from_view': 'blah blah blah'
        }
        self.user = User.objects.create(id=100,username='jubril', password='issa')
        self.user.set_password('shuaib')
        self.user.save()
        self.login = self.client.login(username='jubril', password='shuaib')
        self.notification = Notification.objects.create(id=100,content="Python",
                                                        user=self.user, read=False, link="link",
                                                        activity_type="Vote")


    def test_that_middleware_updates_context_with_categories(self):
        """
        tests that the response context_data was updated with
        correct data for activies and unread fileds
        """
        response = self.client.get(reverse('user_profile', kwargs={'username': self.user.username}))
        # there is activities
        activities = response.context_data.get('activities')
        self.assertEqual(len(activities),1)
        self.assertIsNotNone(activities)
        # assert for unread
        unread = response.context_data.get('unread')
        self.assertIsNotNone(unread)
        self.assertEqual(len(unread),1)



    def test_that_middleware_retains_previous_context_data(self):
        """
        tests that the response context_data set in the views is not
        discarded or overwritten in the middleware.
        """
        response = self.activity.process_template_response(
            self.request,
            self.response
        )
        # assert for previous data
        prev_context_data = response.context_data.get('context_var_from_view')
        self.assertIsNotNone(prev_context_data)
        self.assertEqual(prev_context_data, 'blah blah blah')