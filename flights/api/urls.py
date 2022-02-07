from django.contrib import admin
from django.db.models import base
from django.urls import path
from django.urls.conf import include
from . views import FlightViewSet, DetailViewSet
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt



router = DefaultRouter()
router.register(r'flights', FlightViewSet)
router.register(r'details', DetailViewSet)
# router.register(r'flight-details', DetailViewSet, basename='flight-details')

urlpatterns = [
    path('', include(router.urls)),
    path('flightdetails/<int:pk>', DetailViewSet.as_view({'get': 'list'}), name='flight-details'),
    # path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    # path('flights/<int:pk>')
    # .as_view({'get': 'list'})
]