from django.shortcuts import render
from .models import Airport
from django.http import HttpResponse
import random

# Create your views here.
def airport_view(request):
    airports = random.choice(Airport.objects.all())
    print(airports)
# 
    # for i in airports:
        # print(print(i))

    
    
    # shuffled_airports = random.shuffle(airports)

    # print(type(airports))
    # print('-----'*40)
    # airport_list = []

    # for i in airports:
        # airport_list.append(i['name'])
        # print(i['name'])
    # print(shuffled_airports)

    # print(airport_list)

    # departure_airport = airport_list[0:18]
    # destination_airport = airport_list[18:37]
    # print(departure_airport)
    # print('-----'*40)
    # print(destination_airport)
    # # print('departure_airport numbers: {} ; destination_airport: {}'.format(len(departure_airport), len(destination_airport)))
    return HttpResponse('Page working!')
