from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing Booking instances.
    """
    list_display = (
        'user', 'date_arrival', 'time_arrival', 'date_leave', 'time_leave')
    list_display_links = (
        'user', 'date_arrival', 'time_arrival', 'date_leave', 'time_leave')
    list_filter = (
        'user', 'date_arrival', 'time_arrival', 'date_leave', 'time_leave')
    search_fields = (
        'user__username', 'treatment__header',)


admin.site.register(Booking, BookingAdmin)
