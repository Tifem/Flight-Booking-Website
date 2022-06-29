from django.contrib import admin
from .models import Booking, Passenger

# Register your models here.


class BookingAdmin(admin.ModelAdmin):
    search_fields = ['reference_no', 'passengers__name','flight__aeroplane']
    list_display = ['reference_no','flight','booking_datetime']
    list_filter = ['passengers']

    date_hierarchy = 'booking_datetime'

admin.site.register(Booking, BookingAdmin)
admin.site.register(Passenger)