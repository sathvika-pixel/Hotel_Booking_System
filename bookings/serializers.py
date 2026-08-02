from rest_framework import serializers
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):

    hotel_name = serializers.CharField(
        source='hotel.name',
        read_only=True
    )

    username = serializers.CharField(
        source='user.username',
        read_only=True
    )

    class Meta:
        model = Booking
        fields = [
            'id',
            'user',
            'username',
            'hotel',
            'hotel_name',
            'check_in',
            'check_out',
            'guests',
            'total_price',
            'status',
            'booked_on'
        ]