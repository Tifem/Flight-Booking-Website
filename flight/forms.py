from django import forms
from django_countries.widgets import CountrySelectWidget
from airport.models import Airport

class AirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = ('name', 'country')
        widgets = {'country': CountrySelectWidget()}