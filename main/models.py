from django.db import models
from cloudinary.models import CloudinaryField

class CarouselImage(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True)
    image = CloudinaryField('image')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['title', 'order']

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = CloudinaryField('image')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
