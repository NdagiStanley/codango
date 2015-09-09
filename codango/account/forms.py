from django import forms


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
