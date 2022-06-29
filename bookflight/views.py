from urllib.request import Request
from django.shortcuts import render
from flight.forms import AirportForm
from flight.models import Flight
from airport.models import Airport
from django.utils import timezone

def landing_page(request):

    flights = Flight.objects.all().order_by('departure_datetime')
    airports = Airport.objects.all()

    departure_airport = request.GET.get('departure_airport')
    destination_airport = request.GET.get('destination_airport')
    departure_date = request.GET.get('departure_date')
    arrival_date = request.GET.get('arrival_date')


    def is_validparam(param):
        return param != '' and param is not None

    if is_validparam(departure_airport):
        flights = flights.filter(departure_datetime__gte=timezone.now(), departure__country__name=departure_airport)

    if is_validparam(destination_airport):
        flights = flights.filter(departure_datetime__gte=timezone.now(), destination__country__name=destination_airport)

    if is_validparam(departure_date):
        flights = flights.filter(departure_datetime__gte=departure_date)

    if is_validparam(arrival_date):
        flights = flights.filter(arrival_datetime__lt=arrival_date)

    context  = {
        # 'form':AirportForm(),
        'flights':flights,
        'airports':airports,
        
        'departure_airport':departure_airport,
        'destination_airport':destination_airport,
        'departure_date':departure_date,
        'arrival_date':arrival_date,

    }

    return render(request, 'landing_page.html', context=context)
