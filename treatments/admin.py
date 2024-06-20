from django.contrib import admin
from .models import Section, Treatment
from django_summernote.admin import SummernoteModelAdmin

class TreatmentInline(admin.StackedInline):
    model = Treatment
    extra = 1

@admin.register(Section)
class SectionAdmin(SummernoteModelAdmin):
    inlines = [TreatmentInline]
    summernote_fields = '__all__'

