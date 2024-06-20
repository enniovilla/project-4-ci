from django import forms
from .models import Booking

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date_arrival', 'time_arrival', 'date_leave', 'time_leave']
        widgets = {
            'user': forms.HiddenInput,
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
