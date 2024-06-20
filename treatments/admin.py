from django.contrib import admin
from .models import Section, Treatment

class TreatmentInline(admin.StackedInline):
    model = Treatment
    extra = 1

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    inlines = [TreatmentInline]

