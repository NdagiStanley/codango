from django.test import TestCase
from account.emails import send_mail

class EmailTestCase(TestCase):
    
    def setUp(self):
        self.email =  send_mail.compose(
            sender = 'Codango Tests <codango@andela.com>',
            reciepient = 'awillionaire@gmail',
            subject = 'Codango Email Integration With Mailgun (Tests)',
            html = "<p>Codango</p>",
            text = "Codango Testing",
        )
    
    def test_send_email_returns_request_status(self):
        response = send_mail.send(self.email)
        self.assertEqual(response, 200)