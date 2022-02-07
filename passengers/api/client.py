from inspect import trace
from google.protobuf import message
from google.protobuf.json_format import MessageToDict
from rest_framework.fields import empty
from rest_framework import serializers
from rest_framework.response import Response
from passengers.settings import FLIGHT_GRPC
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


def get_flight_details(request):
    responeDetails = []

    with grpc.insecure_channel(FLIGHT_GRPC) as channel:
        try:
            stub = flights_pb2_grpc.FlightsStub(channel)
            for details in stub.getDetails(flights_pb2.userdetailrequest()):
                response = details
                response = MessageToDict(response)
                responeDetails.append(response)
        except Exception as e:
            traceback.print_exc()
        channel.close()
    return(responeDetails)



def get_seat(request):
    responseSeat = []

    with grpc.insecure_channel(FLIGHT_GRPC) as channel:
        try:
            stub = flights_pb2_grpc.FlightsStub(channel)
            for seats in stub.getSeats(flights_pb2.userseatrequest()):
                respone = seats
                respone = MessageToDict(respone)
                responseSeat.append(respone)
        except Exception as e:
            traceback.print_exc()
        channel.close()
    return(responseSeat)


def flight_create(request):
    with grpc.insecure_channel(FLIGHT_GRPC) as channel:
        response = 0
        try:
            stub = flights_pb2_grpc.FlightsStub(channel)
            response = stub.setFlights(flights_pb2.flightcreate(
                flightCode=request['flightCode'],
                airlineName=request['airlineName'],
                departureLocation=request['departureLocation'],
                arrivalLocation=request['arrivalLocation'],
                departureTime=request['departureTime'],
                arrivalTime=request['arrivalTime'],
                duration=request['duration'],
                planeModel=request['planeModel'],
                totalSeats=request['totalSeats'],
                userID=request['userID'],
            ))
            response = MessageToDict(response)
            #return response
        except Exception as e:
            traceback.print_exc()
        channel.close()
    return response

def detail_create(request):
    with grpc.insecure_channel(FLIGHT_GRPC) as channel:
        response = 0
        try:
            stub = flights_pb2_grpc.FlightsStub(channel)
            response = stub.setDetails(flights_pb2.detailcreate(
                departureDate = request['departureDate'],
                price = request['price'],
                flightStatus = request['flightStatus'],
                userID = request['userID'],
                flightfk = request['flightfk'],
            ))
            response = MessageToDict(response)
        except Exception as e:
            traceback.print_exc()
        channel.close()
    return response

def seat_create(request):
    with grpc.insecure_channel(FLIGHT_GRPC) as channel:
        response = 0
        try:
            stub = flights_pb2_grpc.FlightsStub(channel)
            response = stub.setSeat(flights_pb2.seatcreate(
                seatClass = request['seatClass'],
                seatNumber = request['seatNumber'],
                booked = request['booked'],
            ))
            response = MessageToDict(response)
        except Exception as e:
            traceback.print_exc()
        channel.close()
    return response