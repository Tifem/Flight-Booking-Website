from django.shortcuts import render
from .models import Flight
from airport.models import Airport
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def flight_search(request):
    template = 'flight/flight_search.html'

    flights = Flight.objects.all().order_by('departure_datetime')
    departure_airport = request.GET.get('departure_airport')
    destination_airport = request.GET.get('destination_airport')
    departure_date = request.GET.get('departure_date')
    arrival_date = request.GET.get('arrival_date')

    def is_validparam(param):
        return param != '' and param is not None


    if is_validparam(departure_airport):
        # flights = flights.filter(departure_datetime__gte=timezone.now(), departure__country__startswith=departure_airport)
        flights = flights.filter(departure__country__istartswith=departure_airport)

    if is_validparam(destination_airport):
        flights = flights.filter(destination__country__istartswith=destination_airport)

    if is_validparam(departure_date):
        flights = flights.filter(departure_datetime__gte=departure_date)

    if is_validparam(arrival_date):
        flights = flights.filter(arrival_datetime__lt=arrival_date)

    context  = {
        'flights':flights,        
        'departure_airport':departure_airport,
        'destination_airport':destination_airport,
        'departure_date':departure_date,
        'arrival_date':arrival_date,

    }

    if request.htmx:
        template = 'flight/partials/search.html'
        departure_airport = request.GET.get('departure_airport')
        destination_airport = request.GET.get('destination_airport')
        departure_date = request.GET.get('departure_date')
        arrival_date = request.GET.get('arrival_date')

        if is_validparam(departure_airport):
            # flights = flights.filter(departure_datetime__gte=timezone.now(), departure__country__startswith=departure_airport)
            flights = flights.filter(departure__country__istartswith=departure_airport)

        elif is_validparam(destination_airport):
            # flights = flights.filter(departure_datetime__gte=timezone.now(), destination__country__name=destination_airport)

            flights = flights.filter(destination__country__istartswith=destination_airport)
        # else:
            # return HttpResponse('')
        elif is_validparam(departure_date):
            flights = flights.filter(departure_datetime__gte=departure_date)

        elif is_validparam(arrival_date):
            flights = flights.filter(arrival_datetime__lt=arrival_date)

        else:
            return HttpResponse('')
   
   

    return render(request, template, context=context)

def flight_detail(request, pk):

    flight = Flight.objects.get(pk=pk)
    bookings = flight.booking_flight.all()
    price = flight.price

    for booking in bookings:
        passenger_count = booking.passengers.all().count()

    total_money = price * passenger_count

    context = {
        'flight':flight,
        'bookings':bookings,
        'total_money':total_money,
    }

    return render(request, 'flight/flight_detail.html', context)

