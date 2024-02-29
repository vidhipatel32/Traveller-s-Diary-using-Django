from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking

def booking_form(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()  # Save the form data to the database and get the instance
            return render(request, 'book_details.html', {'booking': booking})
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})
