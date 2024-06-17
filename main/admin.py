from django.contrib import admin
from .models import CarouselImage, Welcome, Discover

class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)


class WelcomeAdmin(admin.ModelAdmin):
    list_display = ('heading', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('is_active',)


class DiscoverAdmin(admin.ModelAdmin):
    list_display = ('heading', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('is_active',)


admin.site.register(CarouselImage, CarouselImageAdmin)
admin.site.register(Welcome, WelcomeAdmin)
admin.site.register(Discover, DiscoverAdmin)
