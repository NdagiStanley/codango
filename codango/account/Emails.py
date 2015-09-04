from django.shortcuts import render
from django.template import RequestContext, loader
import requests

class MailSender:

	def send_mail():
	    return requests.post(
	        "https://api.mailgun.net/v3/sandboxb2b5451c43284f7a8bc19a345ab06b2e.mailgun.org",
	        auth=("api", "key-63b86d9d5953b932e5af3c1ad6f2ae4b"),
	        files=[("attachment", open("files/test.jpg")),
	               ("attachment", open("files/test.txt"))],
	        data={"from": "Excited User <inioluwafageyinbo@gmail.com>",
	              "to": "foo@example.com",
	              "cc": "baz@example.com",
	              "bcc": "bar@example.com",
	              "subject": "Password Recovery",
	              "text": "Open this link to reset your password!",
	              "html": "<html>HTML version of the body</html>"})