
from django import forms
from .models import *
from django.contrib.auth.models import User

class ImagePostForm(forms.ModelForm):
    class Meta:
        model = ImagePost
        fields = ['image', 'description']  # Include any other fields as needed


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User  # Use Django's built-in User model
        fields = ['first_name', 'last_name', 'email']




class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile  # Profile model is assumed to have user-specific fields
        fields = ['image', 'bio']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
        }

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
