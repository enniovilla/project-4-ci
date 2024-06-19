from django.contrib import admin
from .models import Section, AccordionItem
from django_summernote.admin import SummernoteModelAdmin

class AccordionItemInline(admin.StackedInline):
    model = AccordionItem
    extra = 1

@admin.register(Section)
class SectionAdmin(SummernoteModelAdmin):
    inlines = [AccordionItemInline]
    summernote_fields = '__all__'

