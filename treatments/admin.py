from django.contrib import admin
from .models import Section, Treatment


class TreatmentInline(admin.StackedInline):
    """
    Defines an inline model for treatments within the Section admin.
    Attributes:
    - model: Specifies the Treatment model to be displayed inline.
    - extra: Controls the number of extra Treatment forms to display.
    """
    model = Treatment
    extra = 1


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing Section instances.
    The inlines specifies inline models to include within the Section admin,
    here including TreatmentInline to manage treatments directly from the
    Section admin page.
    """
    inlines = [TreatmentInline]
