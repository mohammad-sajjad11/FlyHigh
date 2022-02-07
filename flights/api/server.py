from inspect import trace
import re
from typing import List

from . import flights_pb2_grpc
from . import flights_pb2
import grpc
import traceback
from google.protobuf.json_format import MessageToDict
from .models import Flight, FlightDetails, Seating
from .serializers import FlightSerializer, FlightDetailsSerializer, SeatingSerailizer

class FlightListener(flights_pb2_grpc.FlightsServicer):
    def getFlights(self, request, context):
        try:
            request = MessageToDict(request)
            queryset = Flight.objects.filter(id__gte=1)
            response = FlightSerializer(data=queryset, many=True)
            if response.is_valid(raise_exception=False):
                print('Response is valid and proceeding further', response.data)
            else:
                print('Errors in getFlights, server', response.errors)
            for i in response.data:
                yield flights_pb2.FlightResponse(**i)
        except Exception as e:
            traceback.print_exc()

    def getDetails(self, request, context):
        try:
            request = MessageToDict(request)
            # Flight.objects.get(pk=request)
            # queryset = f.choice_set.all(), context={'request': request}
            queryset = FlightDetails.objects.filter(id__gte=1)
            response = FlightDetailsSerializer(data=queryset, many=True)
            if response.is_valid():
                print('Response is valid and proceeding further')
            else:
                print('Errors in getDetails, server', response.errors)
            for i in response.data:
                yield flights_pb2.DetailResponse(**i)
        except Exception as e:
            traceback.print_exc()
            # return(ExceptionString=e.args[0])

    def getSeats(self, request, context):
        try:
            request = MessageToDict(request)
            queryset = Seating.objects.filter(id__gte=1)
            response = SeatingSerailizer(data=queryset, many=True)
            if response.is_valid():
                print('Response is valid and proceeding further')
            else:
                print('Error in getSeats, server', response.errors)
            for i in response.data:
                yield flights_pb2.SeatResponse(**i)
        except Exception as e:
            traceback.print_exc()
            # return(ExceptionString=e.args[0])
    
    def setFlights(self, request, context):
        try:
            request = MessageToDict(request)
            response = FlightSerializer(data=request)
            if response.is_valid():
                print('response valid in set flight in server, proceeding further')
            else:
                print('Errors in setFlights', response.errors)
            response = Flight.objects.create(**request)
            returnResponse = {
                "success" : True
            }
            return flights_pb2.flightcreateresponse(**returnResponse)
        except Exception as e:
              traceback.print_exc()
            
    def setDetails(self, request, context):
        try:
            request = MessageToDict(request)
            s = request["flightfk"]
            # print('SSS', s)
            # print('type SSS', type(s))
            a = Flight.objects.get(id = s)
            request['flightfk'] = a
            response = FlightDetailsSerializer(data=request)
            if response.is_valid():
                print('response valid in set details in server, proceeding further')
            else:
                print('Error in setDetails', response.errors)
            response = FlightDetails.objects.create(**request)
            returnResponse = {
                "success" : True
            }
            return flights_pb2.flightcreateresponse(**returnResponse)
        except Exception as e:
              traceback.print_exc()
              




def grpc_hook(server):
    flights_pb2_grpc.add_FlightsServicer_to_server(FlightListener(), server)