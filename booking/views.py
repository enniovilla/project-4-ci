from django.shortcuts import render, redirect
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from .models import Booking


@login_required
def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            form.save()
            return render(request, 'booking/booking_success.html', {'booking': booking})

    else:
        form = BookingForm()

    context = {
        'form': form,
    }
    return render(request, 'booking/booking.html', context)


@login_required
def my_bookings(request):
        bookings = Booking.objects.filter(user=request.user)
        context = {
            'bookings': bookings
        }
        return render(request, 'booking/my_bookings.html', context)