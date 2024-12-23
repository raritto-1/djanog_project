# forms.py
from django import forms
from .models import UploadImagePost

class UploadImagePostForm(forms.ModelForm):
    class Meta:
        model = UploadImagePost
        fields = ['title', 'image']
