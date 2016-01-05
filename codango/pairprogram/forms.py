from django import forms
from models import Session
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


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