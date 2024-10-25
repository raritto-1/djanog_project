# qr_app/forms.py

from django import forms

class QRCodeForm(forms.Form):
    link = forms.URLField(label='Enter your link', max_length=200)
