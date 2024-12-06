from django.contrib import admin
from .models import UserProfile  # Import your custom user profile model

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'displayname', 'info')  # Display key fields in the admin list view
    search_fields = ('user__username', 'displayname')  # Enable searching by the related user's username and displayname
    list_filter = ('user',)  # Add filtering options for user field

