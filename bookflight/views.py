from urllib.request import Request
from django.shortcuts import render
from flight.models import Flight
from airport.models import Airport
from django.utils import timezone
from django.http import Http404, HttpResponse



def landing_page(request):

    template = 'landing_page.html'
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
        'flights':flights[:5],
        'departure_airport':departure_airport,
        'destination_airport':destination_airport,
        'departure_date':departure_date,
        'arrival_date':arrival_date,

    }

    if request.htmx:
    # flights = flights.filter(departure__country__startswith=departure_airport)[:5]
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
