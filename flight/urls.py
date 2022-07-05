from django.urls import path
from flight import views

app_name = 'flight'

urlpatterns = [

    path('search/', views.flight_search, name='flight-search'),
    path('<int:pk>/', views.flight_detail, name='flight-detail'),
]
