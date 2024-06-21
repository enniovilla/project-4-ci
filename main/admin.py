from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import CarouselImage, Welcome


@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing CarouselImage instances.
    """
    list_display = ('title', 'order')
    list_editable = ('order',)


@admin.register(Welcome)
class WelcomeAdmin(SummernoteModelAdmin):
    """
    Admin configuration for managing Welcome instances,
    using Summernote for the paragraph field.
    """
    list_display = ('heading', 'is_active')