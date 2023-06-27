from django import forms 

class UserForm(forms.Form):
    username = forms.CharField(max_length=255)
    email = forms.EmailField()
    password = forms.CharField(max_length=155)
    country = forms.CharField(max_length=255)
    