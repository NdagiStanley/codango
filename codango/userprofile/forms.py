from django import forms
from models import UserProfile


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
