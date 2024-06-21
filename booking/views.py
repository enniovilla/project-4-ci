from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Booking


@login_required
def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            form.save()
            return render(
                request, 'booking/booking_success.html', {'booking': booking})

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


@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking edited successfully.')
            return redirect('my_bookings')
    else:
        form = BookingForm(instance=booking)
    context = {
        'form': form,
        'booking': booking,
    }
    return render(request, 'booking/edit_booking.html', context)


@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Booking deleted successfully.')
        return redirect('my_bookings')
    context = {
        'booking': booking,
    }
    return render(request, 'booking/delete_booking.html', context)
