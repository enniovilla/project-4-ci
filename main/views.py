from django.shortcuts import render
from .models import CarouselImage

def home(request):
    image = CarouselImage.objects.all()
    return render(request, 'main/index.html', {'image': image})
