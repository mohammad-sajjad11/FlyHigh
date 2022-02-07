from typing import Tuple
from django.db import models
import datetime
# Create your models here.

class Flight(models.Model):
    flightCode = models.TextField(max_length=7, blank=False)

    airlineName = models.CharField(max_length=15, blank=False)

    departureLocation = models.CharField(max_length=20, blank=False)

    arrivalLocation = models.CharField(max_length=15, blank=False)

    departureTime = models.TimeField(blank=False)

    arrivalTime = models.TimeField(blank=False)

    duration = models.CharField(blank=False, max_length=6)

    planeModel = models.CharField(max_length=20, null=True, default="")

    totalSeats = models.IntegerField(default=40)

    userID = models.IntegerField(null=True, blank=True)

class FlightDetails(models.Model):    
    departureDate = models.DateField(blank=False)

    price = models.IntegerField(blank=True, null=True)

    # seating = models.ForeignKey(Seating, on_delete=models.SET_NULL, null=True)

    flightStatus = models.BooleanField(blank=False, null=True)

    userID = models.IntegerField(null=True)

    flightfk = models.ForeignKey(Flight, on_delete=models.CASCADE, to_field='id')   

class Seating(models.Model):
    # class seats(models.IntegerChoices):
    #     A = 1
    #     B = 2
    #     C = 3
    #     D = 4

    seats = (
        (1,'A'),
        (2,'B'),
        (3,'C'),
        (4,'D'),
    )

    seatClass = models.IntegerField(choices=seats)

    seatNumber = models.IntegerField(null=True)
    
    booked = models.BooleanField(default=False)

    flightdetailid = models.ForeignKey(FlightDetails, on_delete=models.CASCADE, null = True)







