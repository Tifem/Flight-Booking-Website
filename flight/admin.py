from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Flight

# Register your models here.
class FlightAdmin(admin.ModelAdmin):

    search_fields = ['aeroplane','departure__name','destination__name','max_passengers']
    date_hierarchy = 'departure_datetime'
    readonly_fields = ['duration']
    list_filter = ['departure_datetime', 'arrival_datetime']
    list_display= ['aeroplane','departure','destination','departure_datetime',
                'arrival_datetime','duration','max_passengers', 'price']
    
     

    
admin.site.site_header = 'BookFlight Administration'
admin.site.site_title = 'BookFlight Admin'
admin.site.index_title = 'Manage BookFlight'
admin.site.register(Flight, FlightAdmin)