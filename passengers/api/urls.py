from django.urls import path, include
from rest_framework import routers, urlpatterns

from . import views

router = routers.DefaultRouter()
router.register(r'flights', views.Flights, basename='flights')
router.register(r'flightdetails', views.FlightDetails, basename='details')




urlpatterns = [
    path('', include(router.urls)),
    # path('flightdetails/<int:id>', views.FlightDetails.as_view(
    #         {
    #             'get':'list'
    #         }
    #     ),name='flight-details'),
    # path('', include(router.urls)),
    # path('check', views.Flights.as_view(
    #     {
    #         'get':'list',
    #         'post':'create'
    #    }
    # ))
]