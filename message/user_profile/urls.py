from django.urls import path
from . import views
# from django.contrib.auth import views as log
urlpatterns = [
    path('', views.home, name='home'),  # Home page
    
   path('login_page/', views.login_page, name='login_page'),

    path('register/', views.register_page, name='register'),  # Register page
    path('profile/', views.profile_page, name='profile_page'),  # Profile page
    path('log_out/', views.log_out, name='log_out'),   # Logout functionality
]