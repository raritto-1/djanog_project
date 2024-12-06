from django import forms
from .models import User  # Import the User model to reference it in the form

class MessageForm(forms.Form):
    sender = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Sender"
    )
    receiver = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Receiver"
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Write your message here...', 'class': 'form-control'}),
        label="Message"
    )
