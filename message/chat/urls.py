from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_home, name='chat_home'),  # Home page for the chat app
    path('room/<int:sender_id>/<int:receiver_id>/', views.chat_room, name='chat_room'),  # Chat room URL

]