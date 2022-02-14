from django.http import response
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import action, api_view, APIView
from rest_framework.response import Response
from rest_framework import viewsets, status
import json

# Create your views here.

from django.http.response import HttpResponse

from .serializers import FlightDetailsSerializer, FlightSerializer, SeatSerializer
from . import client

class Flights(viewsets.ViewSet):
    def list(self, request):
        response = client.get_flights(request)
        return Response(response)

    def create(self, request):
        serializer = FlightSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            response = client.flight_create(request.data)
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FlightDetails(viewsets.ViewSet):
    def list(self, request):
        response = client.get_flight_details(request)
        return Response(response)

    def create(self, request):
        serializer = FlightDetailsSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            response = client.detail_create(request.data)
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Seat(viewsets.ViewSet):

    def create(self, request):
        serializer = SeatSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            response = client.seat_create(request.data)
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
