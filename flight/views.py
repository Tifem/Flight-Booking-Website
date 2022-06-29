from django.shortcuts import render
from .models import Flight

# Create your views here.
def flight_detail(request, pk):

    flight = Flight.objects.get(pk=pk)
    bookings = flight.booking_flight.all()


    context = {
        'flight':flight,
        'bookings':bookings,
    }

    return render(request, 'flight/flight_detail.html', context)