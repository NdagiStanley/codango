from django import forms


class ResetForm(forms.Form):
    
    password = forms.CharField(label='New Password', required=True, max_length=200, widget=forms.PasswordInput())

    password_conf = forms.CharField(label='Confirm New Password', required=True, max_length=200, widget=forms.PasswordInput())
