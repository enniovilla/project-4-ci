from django.shortcuts import render
from .models import CarouselImage, Welcome


def home(request):
    """
    Renders the home page view with carousel images and a welcome message.
    Retrieves all CarouselImage objects
    and the first Welcome object from the database.
    These objects are passed as context to
    render the 'main/index.html' template,
    which represents the home page of the website.
    """
    image = CarouselImage.objects.all()
    welcome = Welcome.objects.filter().first()

    context = {
        'image': image,
        'welcome': welcome,
    }
    return render(request, 'main/index.html', context)
