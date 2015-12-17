from django.test import TestCase
from resources.tasks import send_recent_posts
from mock import patch
from account.emails import SendGrid


class PopularPostUpdateTestCase(TestCase):

    # mocking sendgrid's send method

    @patch.object(SendGrid, 'send')
    def test_no_error(self, mock_method):
        """
        Test that the ``scheduled task`` task runs successfully.
        """
        # test that mails would send daily
        result = send_recent_posts.delay('daily')
        self.assertTrue(result.successful())
        self.assertFalse(result.failed())

        # test that mails would send weekly
        result = send_recent_posts.delay('weekly')
        self.assertTrue(result.successful())
        self.assertFalse(result.failed())

        # test that mails would send monthly
        result = send_recent_posts.delay('monthly')
        self.assertTrue(result.successful())
        self.assertFalse(result.failed())
