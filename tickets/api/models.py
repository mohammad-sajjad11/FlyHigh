import uuid
from django.db import models
import uuid
# Create your models here.

class Ticket(models.Model):
    reference = models.UUIDField(default = uuid.uuid4)

    passengerID = models.IntegerField(null=True, unique=True)

    flightDetailsID = models.IntegerField(null=True)