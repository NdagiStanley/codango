from django import forms
from models import UserProfile
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name',
                  'place_of_work', 'position', 'about', 'image']
        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'place_of_work': 'Place of work',
            'position': 'Position',
            'about': 'About'
        }


class NotificationPreferenceForm(forms.Form):
    comment_notification = forms.BooleanField(
        label='Receive comment notifications',
        widget=forms.CheckboxInput
    )

    like_notification = forms.BooleanField(
        label='Receive likes notifications',
        widget=forms.CheckboxInput
    )


class ChangeUsernameForm(forms.Form):
    new_username = forms.CharField(
        label='New Username', max_length=100,
        validators=[RegexValidator(
            r'^[0-9a-zA-Z_]*$')],
        widget=forms.TextInput(attrs={
            'placeholder': 'Type in your new username',
            'autocomplete': 'off'
        }))

    def clean_new_username(self):
        try:
            User.objects.get(username=self.cleaned_data['new_username'])
        except User.DoesNotExist:
            return self.cleaned_data['new_username']
        raise forms.ValidationError(
            "This username is taken")


class ChangePasswordForm(forms.Form):
    new_password = forms.CharField(
        label='New Password', max_length=100,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Type in your new password'
        }))

    verify_new_password = forms.CharField(
        label='Confirm New Password', max_length=100,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Verify your new password'
        }))

    def clean(self):
        if 'new_password' in self.cleaned_data and 'verify_new_password' in self.cleaned_data:
            if self.cleaned_data['new_password'] != self.cleaned_data['verify_new_password']:
                raise forms.ValidationError(
                    "You must type in the same password each time")
        return self.cleaned_data
