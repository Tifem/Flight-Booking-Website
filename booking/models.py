from django.db import models
from django.utils import timezone
from flight.models import Flight
import random
from django.contrib.auth.models import User

# Create your models here.
class Passenger(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    

class Booking(models.Model):
    reference_no = models.PositiveIntegerField(blank=True, null=True)
    passengers = models.ManyToManyField(Passenger, related_name='passengers', blank=True)
    flight = models.ForeignKey(Flight, related_name='booking_flight', on_delete=models.CASCADE)
    booking_datetime = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return str(self.reference_no)


    def save(self, *args, **kwargs):
        self.reference_no = random.randrange(100000, 1000000)

        return super(Booking, self).save(*args, **kwargs)
    
    
    class Meta:
        ordering = ['reference_no']