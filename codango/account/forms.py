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
