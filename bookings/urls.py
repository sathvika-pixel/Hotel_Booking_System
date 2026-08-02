from django.urls import path
from . import views

urlpatterns = [

    path(
        "book/<int:id>/",
        views.book_room,
        name="book_room"
    ),

    path(
        "my-bookings/",
        views.my_bookings,
        name="my_bookings"
    ),

    path(
        "payment/",
        views.payment,
        name="payment"
    ),

]