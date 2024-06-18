from django.shortcuts import render
from .models import Section

def treatments_view(request):
    sections = Section.objects.all()
    
    context = {
        'sections': sections
    }
    return render(request, 'treatments/treatments.html', context)
