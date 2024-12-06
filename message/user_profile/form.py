from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import UserProfile

class Profile_form(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image', 'displayname', 'info']
        widgets = {
            'image': forms.FileInput(),
            'displayname': forms.TextInput(attrs={'placeholder': 'Add display name'}),
            'info': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add information'}),
        }

class EmailForm(ModelForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
        }

class PasswordForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))

    class Meta:
        model = User
        fields = ['password']
