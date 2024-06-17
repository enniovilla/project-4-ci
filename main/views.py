from django.shortcuts import render
from .models import CarouselImage, About

def home(request):
    image = CarouselImage.objects.all()
    about = About.objects.first()

    context = {
        'image': image,
        'about': about,
    }
    return render(request, 'main/index.html', context)

def discover(request):
    return render(request, 'main/discover.html')

def treatments(request):
    return render(request, 'main/treatments.html')

def location(request):
    return render(request, 'main/location.html')