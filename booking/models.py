from django.db import models
from flight.models import Flight
import random

# Create your models here.
class Booking(models.Model):
    reference_no = models.PositiveIntegerField(blank=True, null=True)
    passenger_first_name = models.CharField(max_length=100)
    passenger_last_name = models.CharField(max_length=100)
    flight = models.ForeignKey(Flight, related_name='booking_flight', on_delete=models.CASCADE)
    

    def __str__(self):
        return str(self.reference_no)


    def save(self, *args, **kwargs):
        self.reference_no = random.randrange(100000, 100000001)

        return super(Booking, self).save(*args, **kwargs)
    
    