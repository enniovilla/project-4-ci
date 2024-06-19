# contact/admin.py

from django.contrib import admin
from .models import ContactMessage

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'timestamp')
    search_fields = ('name', 'email', 'subject', 'message')
    date_hierarchy = 'timestamp'

admin.site.register(ContactMessage, ContactMessageAdmin)