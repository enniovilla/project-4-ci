from django.shortcuts import render
from .models import Section

def treatments_view(request):
    """
    Render the treatments view that displays all sections of treatments.

    This view retrieves all Section objects from the database and renders them
    in the 'treatments/treatments.html' template. Each Section represents a
    different treatment category or area of focus. The rendered HTML will
    present these sections to the user, allowing them to explore various
    treatment options available.
    """
    sections = Section.objects.all()
    
    context = {
        'sections': sections
    }
    return render(request, 'treatments/treatments.html', context)
