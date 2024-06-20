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
            'date_arrival': DateInput(),
            'date_leave': DateInput(),
            'time_arrival': TimeInput(),
            'time_leave': TimeInput(),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['user'].initial = user
