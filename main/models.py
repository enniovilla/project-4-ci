from django.db import models
from cloudinary.models import CloudinaryField

class CarouselImage(models.Model):
    image = CloudinaryField('image')
