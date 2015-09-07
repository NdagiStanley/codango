from django.test import TestCase

from account.forms import LoginForm


class LoginFormTest(TestCase):

    def test_form_inputs(self):
        form_data = {
            'username': 'lade',
            'password': 'password',
        }

        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())
