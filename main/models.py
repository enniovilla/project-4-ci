from django.db import models
from cloudinary.models import CloudinaryField


class CarouselImage(models.Model):
    """
    Represents an image displayed in a carousel on the home page.
    """
    title = models.CharField(max_length=50)
    image = CloudinaryField('image')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['title', 'order']

    def __str__(self):
        return self.title


class Welcome(models.Model):
    """
    Represents a welcome message displayed on the home page.
    """
    heading = models.CharField(max_length=200)
    paragraph = models.TextField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.heading
