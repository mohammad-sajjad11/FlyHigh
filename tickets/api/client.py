from inspect import trace
from google.protobuf import message
from google.protobuf.json_format import MessageToDict
from rest_framework.fields import empty
from rest_framework import serializers
from rest_framework.response import Response
from tickets.settings import FLIGHT_GRPC
from . import flights_pb2
from . import flights_pb2_grpc
import grpc
import os
import json
import traceback

def get_flights(request):
    responseFlights = []

    with grpc.insecure_channel(FLIGHT_GRPC) as channel:
        try:
            stub = flights_pb2_grpc.FlightsStub(channel)
            for flights in stub.getFlights(flights_pb2.userflightrequest()):
                response = flights
                response = MessageToDict(response)
                responseFlights.append(response)
        except Exception as e:
            traceback.print_exc()
        channel.close()
    return(responseFlights)