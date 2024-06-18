from django.contrib import admin
from .models import Section, AccordionItem

class AccordionItemInline(admin.StackedInline):
    model = AccordionItem
    extra = 1


class SectionAdmin(admin.ModelAdmin):
    inlines = [AccordionItemInline]

admin.site.register(Section, SectionAdmin)
