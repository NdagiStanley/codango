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
        result = send_recent_posts.delay('test@test.com')
        self.assertTrue(result.successful())
        self.assertFalse(result.failed())
