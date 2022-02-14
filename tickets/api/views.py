from django.http import response
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import action, api_view, APIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
import json

from . import client

# Create your views here.

from .serializers import TicketSerializer

def Basic(request):
        return render(request, 'tickets_main_page.html')

class Flights(viewsets.ViewSet):
    # renderer_classes = (TemplateHTMLRenderer, JSONRenderer)
    # template_name = 'all_flights.html'

    def list(self, request):
        response = client.get_flights(request)
        print('Response TYPE', type(response))
        # return render(Response(response))
        # return Response({'flights': response}, template_name='all_flights.html')
        return render(request, 'all_flights.html', {'flights': response})


        