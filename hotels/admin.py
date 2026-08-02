from django.contrib import admin
from .models import Hotel


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'city',
        'hotel_type',
        'price_per_night',
        'available_rooms',
        'rating'
    )

    list_filter = (
        'city',
        'hotel_type'
    )

    search_fields = (
        'name',
        'city'
    )