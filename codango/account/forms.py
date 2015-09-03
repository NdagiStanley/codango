from django import forms


class LoginForm(forms.Form):

    username = forms.EmailField(label='Email', max_length=100,
                                widget=forms.EmailInput(attrs={
                                    'placeholder': 'john.doe@example.com'
                                }))
    password = forms.CharField(label='Password', max_length=100,
                               widget=forms.PasswordInput(attrs={
                                   'placeholder': 'Enter secret password'
                               }))
