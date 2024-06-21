from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'timestamp')
    list_display_links = ('name', 'email', 'subject')
    list_filter = ('name', 'email', 'timestamp')
    search_fields = ('name', 'email', 'subject',)
    date_hierarchy = 'timestamp'