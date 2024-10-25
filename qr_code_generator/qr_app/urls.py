# qr_app/urls.py

from django.urls import path
from .views import generate_qr

urlpatterns = [
    path('', generate_qr, name='generate_qr'),
]