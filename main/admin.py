from django.contrib import admin
from .models import CarouselImage, Welcome, Discover
from django_summernote.admin import SummernoteModelAdmin

class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)

@admin.register(Welcome)
class WelcomeAdmin(SummernoteModelAdmin):
    list_display = ('heading', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('is_active',)

@admin.register(Discover)
class DiscoverAdmin(SummernoteModelAdmin):
    list_display = ('heading', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('is_active',)


admin.site.register(CarouselImage, CarouselImageAdmin)
