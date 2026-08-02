from django.shortcuts import render, get_object_or_404
from .models import Hotel


def home(request):
    hotels = Hotel.objects.all()[:6]

    context = {
        "hotels": hotels
    }

    return render(request, "hotels/home.html", context)


def hotel_list(request):
    hotels = Hotel.objects.all()

    context = {
        "hotels": hotels
    }

    return render(request, "hotels/hotel_list.html", context)


def hotel_detail(request, id):
    hotel = get_object_or_404(
        Hotel,
        id=id
    )

    context = {
        "hotel": hotel
    }

    return render(request, "hotels/hotel_detail.html", context)

# Create your views here.
