from ast import Try
from cgitb import lookup
from email.policy import default
from re import search
import traceback
from django.db import models
from django.db.models import fields
from django.db.models.enums import Choices
from django.views.decorators.csrf import requires_csrf_token
from rest_framework import serializers
from rest_framework.fields import ChoiceField
from api.models import Passenger, ManagementUser
from django.core.validators import MinValueValidator, MaxValueValidator


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'

class ManagementUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagementUser
        fields = '__all__'

class FlightSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    flightCode = serializers.CharField(required=True, max_length=6)

    airlineName = serializers.CharField(required=True, max_length=15)

    departureLocation = serializers.CharField(required=True, max_length=20)

    arrivalLocation = serializers.CharField(required=True, max_length=15)

    departureTime = serializers.TimeField(required=True)

    arrivalTime = serializers.TimeField(required=True)

    duration = serializers.CharField(required=True, max_length=6)

    planeModel = serializers.CharField(max_length=20, allow_blank=True, default="")

    totalSeats = serializers.IntegerField(default=40)

    userID = serializers.IntegerField(allow_null=True, default=None)

    # flightDetails = serializers.HyperlinkedIdentityField(view_name='flight-details')

    # flights = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='flightdetails', lookup_field='pk')

class FlightDetailsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    departureDate = serializers.DateField(required=True)

    price = serializers.IntegerField(allow_null=True)

    flightStatus = serializers.BooleanField(required=True, allow_null=True)

    userID = serializers.IntegerField(allow_null=True)

    flightfk = serializers.IntegerField(allow_null=True)


class SeatSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    seats = (
        (1,'A'),
        (2,'B'),
        (3,'C'),
        (4,'D'),
    )

    seatClass = serializers.ChoiceField(required=True, choices=seats)

    seatNumber = serializers.IntegerField(required=True, max_value=10, min_value=1)

    booked = serializers.BooleanField(default=False)

    flightdetailid = serializers.IntegerField(allow_null=True)
