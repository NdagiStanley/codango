from django.test import TestCase
from account import emails
from account.emails import send_mail

class EmailTestCase(TestCase):
    
    def setUp(self):
        pass
    def test_send_email_returns_request_status(self):
        response = send_mail(
            sender = 'Codango Tests <codango@andela.com>',
            recipient = 'inioluwafageyinbo@gmail',
            subject = 'Codango Email Integration With Mailgun (Tests)',
            html = "<p>Codango</p>",
            text = "Codango Testing",
        )
        self.assertIsInstance(response.status_code, int)