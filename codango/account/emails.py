import sendgrid
from sendgrid import SendGridError, SendGridClientError, SendGridServerError
import os


class SendGrid:

    """
    Using SendGrid email management service
    to handle all email services for Codango
    """

    sg = sendgrid.SendGridClient(
        os.getenv('sendgrid_apikey'),
        raise_errors=True)

    @staticmethod
    def compose(sender, recipient, subject, recipients=None, text="", html=""):

        message = sendgrid.Mail()
        message.add_to(recipient)
        message.add_bcc(recipients)
        message.set_subject(subject)
        message.set_html(html)
        message.set_text(text)
        message.set_from(sender)

        return message

    @staticmethod
    def send(message):

        try:
            http_status_code, message = SendGrid.sg.send(message)
        except SendGridClientError:
            pass
        except SendGridServerError:
            pass

        return http_status_code
