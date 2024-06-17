from django.db import models
from cloudinary.models import CloudinaryField

class CarouselImage(models.Model):
    title = models.CharField(max_length=30, default='default title')
    paragraph = models.CharField(max_length=100, default='default paragaph')
    image = CloudinaryField('image')
