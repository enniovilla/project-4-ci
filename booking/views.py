from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Booking


@login_required
def booking(request):
    """
    Handles the creation of a new booking. If the request method is POST,
    validates the BookingForm data. If valid,
    associates the booking with the current user and saves it.
    Redirects to a success page with the booking details
    upon successful submission.
    If the request method is GET, renders the booking form for user input.
    """
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
    """
    Displays all bookings associated with the current user.
    Retrieves bookings from the database filtered by the current user
    and renders them in the 'booking/my_bookings.html' template.
    """
    bookings = Booking.objects.filter(user=request.user)
    context = {
            'bookings': bookings
        }
    return render(request, 'booking/my_bookings.html', context)


@login_required
def edit_booking(request, booking_id):
    """
    Allows the current user to edit an existing
    booking identified by booking_id. Retrieves
    the booking object and checks if the current
    user is authorized to edit it. If the request method is POST,
    validates the BookingForm data and updates the booking.
    Redirects to 'my_bookings' upon successful editing.
    If the request method is GET, renders the booking edit form pre-filled
    with existing booking details.
    """
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
    """
    Allows the current user to delete an existing booking
    identified by booking_id. Retrieves the booking object and checks
    if the current user is authorized to delete it. If the
    request method is POST, deletes the booking and displays a
    success message. Redirects to 'my_bookings' after successful deletion.
    If the request method is GET, renders
    the confirmation page for deleting the booking.
    """
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Booking deleted successfully.')
        return redirect('my_bookings')
    context = {
        'booking': booking,
    }
    return render(request, 'booking/delete_booking.html', context)
