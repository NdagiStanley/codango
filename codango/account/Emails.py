from django.shortcuts import render
from django.template import RequestContext, loader
import requests


def send_mail(sender, recipient, subject, text=None, html=None):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxb2b5451c43284f7a8bc19a345ab06b2e.mailgun.org/messages",
        auth=("api", "key-63b86d9d5953b932e5af3c1ad6f2ae4b"),
       
        data={"from": sender,
              "to": recipient,
              "subject": subject,
              "text": text,
              "html": html,
        })