from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from hotels.models import Hotel
from .models import Booking
from .forms import BookingForm


@login_required
def book_room(request, id):

    hotel = get_object_or_404(Hotel, id=id)

    if request.method == "POST":

        form = BookingForm(request.POST)

        if form.is_valid():

            booking = form.save(commit=False)

            booking.user = request.user
            booking.hotel = hotel

            nights = (booking.check_out - booking.check_in).days

            booking.total_price = nights * hotel.price_per_night

            booking.status = "Confirmed"

            booking.save()

            hotel.available_rooms -= 1
            hotel.save()

            messages.success(request, "Booking Confirmed Successfully.")

            return redirect("my_bookings")

    else:
        form = BookingForm()

    return render(
        request,
        "booking/booking.html",
        {
            "hotel": hotel,
            "form": form,
        },
    )


@login_required
def my_bookings(request):

    bookings = Booking.objects.filter(user=request.user)

    return render(
        request,
        "booking/my_bookings.html",
        {
            "bookings": bookings,
        },
    )


@login_required
def payment(request):

    return render(request, "booking/payment.html")