from django.db import models
from airport.models import Airport
from django.utils import timezone

# Create your models here.
class Flight(models.Model):
    aeroplane = models.CharField(max_length=200)
    departure = models.ForeignKey(Airport, related_name='flight_departure', on_delete=models.CASCADE)
    destination = models.ForeignKey(Airport, related_name='flight_destination', on_delete=models.CASCADE)
    
    """ coming back to this, not sure if the departure datetime should be created cos flight can be scheduled or departure datetime could be delayed """
    departure_datetime = models.DateTimeField() 
    arrival_datetime = models.DateTimeField()
    max_passengers = models.PositiveIntegerField()
    price = models.PositiveIntegerField()


    @property
    def duration(self):
        duration_difference = self.arrival_datetime - self.departure_datetime
        to_hour = 24
        hours = duration_difference.days * to_hour 

        print('Time(Hours) taken to arrive to destination is {} hours'.format(hours))
        return hours


    def __str__(self):
        return self.aeroplane
    