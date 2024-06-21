from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    """
    Custom form widget for rendering
    date input fields with specific attributes.
    """
    input_type = 'date'


class TimeInput(forms.TimeInput):
    """
    Custom form widget for rendering
    time input fields with specific attributes.
    """
    input_type = 'time'


class BookingForm(forms.ModelForm):
    """
    Form class based on the Booking model for capturing booking details.
    """
    class Meta:
        model = Booking
        fields = ['date_arrival', 'time_arrival', 'date_leave', 'time_leave']
        widgets = {
            'date_arrival': DateInput(attrs={'class': 'form-control fw-bold'}),
            'date_leave': DateInput(attrs={'class': 'form-control fw-bold'}),
            'time_arrival': TimeInput(attrs={'class': 'form-control fw-bold'}),
            'time_leave': TimeInput(attrs={'class': 'form-control fw-bold'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['user'].initial = user
