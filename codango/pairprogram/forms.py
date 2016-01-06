from django import forms
from models import Session


class SessionForm(forms.ModelForm):

    class Meta:
        model = Session
        fields = ['session_name']
        labels = {
            'session_name': 'Session name'
        }
        widgets = {'session_name': forms.TextInput(attrs={
            'required': 'required'
        })}