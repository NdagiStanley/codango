from django import forms


class ResourceForm(forms.ModelForm):
    username = forms.CharField(label='Name', max_length=100)
    title = forms.CharField(label='Title', max_length=100)
    resource = forms.CharField(label='Resource', max_length=2000)
