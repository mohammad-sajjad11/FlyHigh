from django.db import models

# Create your models here.

class Passenger(models.Model):
    passportNumber = models.CharField(unique=True, blank=False, max_length=9)

    firstName  = models.CharField(max_length=10, blank=False)

    lastName = models.CharField(max_length=10, blank=False)

class ManagementUser(models.Model):
    firstName = models.CharField(max_length=10, blank=False)
    lastName = models.CharField(max_length=10, blank=False)

    