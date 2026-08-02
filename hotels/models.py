from django.db import models

class Hotel(models.Model):
    HOTEL_TYPES = [
        ('Luxury', 'Luxury'),
        ('Budget', 'Budget'),
        ('Resort', 'Resort'),
        ('Business', 'Business'),
    ]

    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.TextField()

    hotel_type = models.CharField(
        max_length=20,
        choices=HOTEL_TYPES
    )

    description = models.TextField()

    image = models.ImageField(upload_to='hotel_images/')

    price_per_night = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    available_rooms = models.PositiveIntegerField()

    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=4.5
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
# Create your models here.
