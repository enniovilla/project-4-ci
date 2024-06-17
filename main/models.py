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


class Welcome(models.Model):
    heading = models.CharField(max_length=200)
    paragraph = models.TextField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.heading


class Discover(models.Model):
    heading = models.CharField(max_length=100)
    image = CloudinaryField('image')
    paragraph1 = models.TextField(blank=True)
    paragraph2 = models.TextField(blank=True)
    paragraph3 = models.TextField(blank=True)
    paragraph4 = models.TextField(blank=True)
    paragraph5 = models.TextField(blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.heading