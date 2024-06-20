from django.shortcuts import render
from .models import CarouselImage, Welcome

def home(request):
    image = CarouselImage.objects.all()
    welcome = Welcome.objects.filter().first()

    context = {
        'image': image,
        'welcome': welcome,
    }
    return render(request, 'main/index.html', context)
