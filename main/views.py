from django.shortcuts import render
from .models import CarouselImage

def home(request):
    image = CarouselImage.objects.all()

    context = {
        'image': image,
    }
    return render(request, 'main/index.html', context)

def discover(request):
    return render(request, 'main/discover.html')

def treatments(request):
    return render(request, 'main/treatments.html')

def location(request):
    return render(request, 'main/location.html')