from django.db import models
from django.contrib.auth.models import User

# Room Model
class Room(models.Model):
    ROOM_TYPES = [
        ('Single', 'Single'),
        ('Double', 'Double'),
        ('Suite', 'Suite'),
    ]

    room_id = models.CharField(max_length=10, primary_key=True)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)
    capacity = models.IntegerField()
    price_per_night = models.FloatField()
   
    def __str__(self):
        return f"Room {self.room_id} - {self.room_type}"

# Guest Model
class Guest(models.Model):
    guest_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True) 

    def __str__(self):
        return self.name

# Reservation Model
class Reservation(models.Model):
    PAYMENT_STATUS = [
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
        ('Refunded', 'Refunded'),
    ]

    reservation_id = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.FloatField()
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS)

    def __str__(self):
        return f"Reservation {self.reservation_id} by {self.guest.name}"
