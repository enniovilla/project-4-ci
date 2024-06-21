from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
import datetime


class Booking(models.Model):
    """
    Represents a booking made by a user.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_arrival = models.DateField(default=datetime.date.today)
    date_leave = models.DateField(default=datetime.date.today)
    time_arrival = models.TimeField(default=datetime.time(8))
    time_leave = models.TimeField(default=datetime.time(18))

    def clean(self):
        if self.date_arrival < timezone.now().date():
            raise ValidationError("Arrival date cannot be in the past.")

        if self.date_leave and self.date_leave < timezone.now().date():
            raise ValidationError("Arrival date cannot be in the past.")

    def __str__(self):
        return f'{self.user} booking'


class MyBooking (models.Model):
    """
    Represents a user-specific booking linked to a main Booking.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    my_booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
