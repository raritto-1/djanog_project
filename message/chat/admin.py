from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'text', 'timestamp')
    list_filter = ('sender', 'receiver', 'timestamp')
    search_fields = ('sender__user_name', 'receiver__user_name', 'text')
    ordering = ('-timestamp',)

    def timestamp_display(self, obj):
        return obj.timestamp.strftime('%Y-%m-%d %H:%M:%S')
    timestamp_display.admin_order_field = 'timestamp'
    timestamp_display.short_description = 'Timestamp'
