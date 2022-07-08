from genericpath import exists
from django.core.management import BaseCommand
from faker import Faker
import random
from csv import DictReader
from airport.models import Airport
from flight.models import Flight
from booking.models import Booking, Passenger



departure_airport = ["CALABAR", "ENUGU", "IBADAN", "ILORIN", "JOS", "KADUNA (NEW)", 
                    "MAL'M AMINU INT", "MUR'LA MUH'MED","MAIDUGURI", "PORT HAIRCOURT","SOKOTO", "YOLA"]

departure_country = 'NG'

aeroplane = ['Aero', 'Air Peace', 'Allied Air', 'Arik Air', 'Azman Air', 'Dana Air', 
            'Dornier Aviation Nigeria', 'Green Africa Airways', 'Ibom Air',
            'K-implex Airline','Kanem Air', 'Max Air', 'Overlan Airways', 'TAT Nigeria',
            'United Nigeria Airlines', 'West Link Airlines', 'XEJet',]




price = [40000, 50000, 60000, 70000]

Faker.seed(0)
fake = Faker()


def get_random_aeroplane():
    random_aeroplane = random.choice(aeroplane)

    return random_aeroplane

def get_random_passengers():
    passengers = random.randint(300, 1000)

    return passengers

def get_random_price():
    rand_price = random.choice(price)

    return rand_price


def get_airports():
    airports = Airport.objects.all().values()
    
    
    airport_list = []
    for i in airports:
        airport_list.append(i['name'])

    departure_airport = airport_list[0:18]
    destination_airport = airport_list[18:37]

    return departure_airport, destination_airport

class Command(BaseCommand):

    def add_arguments(self, parser) :
        parser.add_argument('file_name', type=str)


    def handle(self, *args, **options):
        file_name = options['file_name']

        with open(file_name, 'r') as read_obj:
            csv_reader = DictReader(read_obj)
            for row in csv_reader:
                airport_name = row['airport_name']
                country = row['country']
                departure_datetime = row['departure_datetime']
                arrival_datetime = row['arrival_datetime']
                booking_datetime = row['booking_datetime']
                aeroplane = get_random_aeroplane()
                max_passengers = get_random_passengers()
                price = get_random_price()
                
                

                fake_passenger = fake.name()
                

                airport,airport_created = Airport.objects.get_or_create(name=airport_name, country=country)
                departure = random.choice(Airport.objects.all())
                destination = random.choice(Airport.objects.all())


# 
                flight, _ = Flight.objects.get_or_create(aeroplane=aeroplane, departure=departure, destination=destination,
                                            departure_datetime=departure_datetime,arrival_datetime=arrival_datetime,
                                            max_passengers=max_passengers, price=price)

                passenger, _ = Passenger.objects.get_or_create(name=fake_passenger)
                booking, _ = Booking.objects.get_or_create(flight=flight, booking_datetime=booking_datetime)
                for booking_passenger in Passenger.objects.all():
                    booking.passengers.add(booking_passenger)
            self.stdout.write(self.style.SUCCESS('Data Imported Successfully')) 
