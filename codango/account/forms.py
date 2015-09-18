from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):

    username = forms.CharField(label='Username', max_length=100,
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'Enter unique username'
                               }))
    password = forms.CharField(label='Password', max_length=100,
                               widget=forms.PasswordInput(attrs={
                                   'placeholder': 'Enter secret password'
                               }))

    checkbox = forms.BooleanField(label='Remember Me', required=False)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=300)
    email = forms.EmailField()
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())
    password_conf = forms.CharField(
        max_length=100, widget=forms.PasswordInput())


class ResetForm(forms.Form):

    password = forms.CharField(label='New Password', required=True, max_length=200, widget=forms.PasswordInput(
        attrs={
            "placeholder": "Your New Password"
        }
    ))

    password_conf = forms.CharField(label='Confirm New Password', required=True, max_length=200, widget=forms.PasswordInput(
        attrs={
            "placeholder": "Confirm Your New Password"
        }
    ))

    def clean_username(self):
        try:
            User.objects.get(username=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(
            "This user already exist in the database, please choose another username")

    def clean(self):
        if 'password' in self.cleaned_data and 'password_conf' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['password_conf']:
                raise forms.ValidationError(
                    "You must type in the same password each time")
        return self.cleaned_data

    def save(self):
        new_user = User.objects.create_user(username=self.cleaned_data['username'],
                                            email=self.cleaned_data['email'],
                                            password=self.cleaned_data['password'])
        return new_user
