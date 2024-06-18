from django.shortcuts import render
from .models import CarouselImage, Welcome, Discover

def home(request):
    image = CarouselImage.objects.all()
    welcome = Welcome.objects.filter(is_active=True).first()

    context = {
        'image': image,
        'welcome': welcome,
    }
    return render(request, 'main/index.html', context)


def discover(request):
    spa_page_content = Discover.objects.filter(is_active=True).first()

    context = {
        'spa_page_content': spa_page_content
    }
    return render(request, 'main/discover.html', context)
