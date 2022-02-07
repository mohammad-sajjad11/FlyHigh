# FlyHigh

## Flights Management & Ticketing

A very basic flights and ticketing management system as well as booking.

There are three modules in this project: 

- Flight

- Passenger/User

- Ticket

Flight module consists of all the Flight instances and Flight detail instances against a certain flight.

Passenger/User module holds the data to passengers once they book a ticket from ticket module interface(front-end) and their details are saved in passenger module.
Passneger/User module also has the User data, these are the users who have access to manage flights and their details.

Ticket Module has passengerID & flightdetailID that will be binded with the ticket, and a refernece number that will be generated once the tikcet is booked.

The project is microservie based and I am using gRPC for communication between services and a dedicated gRPC server for each module that acts as a server.

The project is still a work in progress, although the communication between Flight/Passenger module and Flight/Ticket module where flight is acting as a server is working.

## Technologies Used
- Python (core)
- Python Django Framework
- Python Django Rest Framework
- gRPC
- Docker

UML Diagram for the project has also been added.

Thank you.
