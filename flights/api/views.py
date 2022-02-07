from django.http import request
from django.shortcuts import render
from rest_framework import viewsets, serializers, renderers, decorators
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Flight, Seating, FlightDetails
from .serializers import FlightDetailsSerializer, FlightSerializer


# Create your views here.

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    # @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    # def flightCode(self, request, *args, **kwargs):
    #     print('This action is executing')

    #     flight = self.get_object()
    #     return Response(flight.id)

class DetailViewSet(viewsets.ModelViewSet):
    queryset = FlightDetails.objects.all()
    serializer_class = FlightDetailsSerializer
    # @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    # def flightdetails(self, request, *args, **kwargs):
    #     print('This action is executing')

    #     flight = self.get_object()
    #     return Response(flight.id)