import imp
from django.forms import fields
from rest_framework import serializers
from .models import Ticket


class TicketSerializer(serializers.Serializer):
    class Meta:
        model = Ticket
        fields = '__all__'