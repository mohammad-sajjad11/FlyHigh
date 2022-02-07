from typing_extensions import Required
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import fields, lookups
from rest_framework import serializers, settings
from api.models import Flight, FlightDetails, Seating
#input_formats=['%H:%M']
from django.conf import settings

class FlightSerializer(serializers.ModelSerializer):
    #departureTime = serializers.TimeField( \input_formats='%H:%M')
    # flightdetails = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='flight-details', lookup_field='pk')
    class Meta:
        model = Flight
        fields = '__all__'
        # fields = ['id', 'flightCode', 'airlineName', 'departureLocation', 'arrivalLocation', 'departureTime', 'arrivalTime', 'duration', 'planeModel', 'totalSeats', 'userID']


class FlightDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightDetails
        fields = '__all__'

class SeatingSerailizer(serializers.ModelSerializer):
    seatNumber = serializers.IntegerField(max_value=10, min_value=0)
    class Meta:
        model = Seating
        fields = ['seatClass', 'seatNumber', 'booked', 'flightdetailid']



    

# class FlightSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)

#     flightCode = serializers.CharField(required=True, allow_blank=False, max_length=4)

#     airlineName = serializers.CharField(max_length=15, allow_blank=False)

#     departureLocation = serializers.CharField(max_length=20, allow_blank=False)

#     arrivalLocation = serializers.CharField(max_length=15, allow_blank=False)

#     departureTime = serializers.TimeField(allow_blank=False)

#     arrivalTime = serializers.TimeField(allow_blank=False)

#     duration = serializers.TimeField(allow_blank=False)

#     planeModel = serializers.CharField(max_length=20, allow_blank=True, default="")

#     totalSeats = serializers.IntegerField(default=40)

#     def create(self, validated_data):
#         return Flight.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.flightCode = validated_data.get('flightCode', instance.flightCode)
#         instance.airlineName = validated_data.get('airlineName', instance.airlineName)
#         instance.departureLocation = validated_data.get('departureLocation', instance.departureLocation)
#         instance.arrivalLocation = validated_data.get('arrivalLocation', instance.arrivalLocation)
#         instance.arrivalLocation = validated_data.get('arrivalLocation', instance.arrivalLocation)
#         instance.arrivalLocation = validated_data.get('arrivalLocation', instance.arrivalLocation)
#         instance.arrivalLocation = validated_data.get('arrivalLocation', instance.arrivalLocation)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance        
