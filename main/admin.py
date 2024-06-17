from django.contrib import admin
from .models import CarouselImage, About

class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)

admin.site.register(CarouselImage, CarouselImageAdmin)
admin.site.register(About)