from django.contrib import admin
from django.urls import path, include
from user_profile.views import login_page

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel URL
    path('user/', include('user_profile.urls')),  # Include user_profile app URLs
    path('', include('chat.urls')), 
    path('login_page', login_page, name = 'login_page') # Set root URL to chat.urls
]
