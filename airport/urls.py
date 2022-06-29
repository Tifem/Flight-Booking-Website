from django.urls import path
from . import views

app_name = 'airport'

urlpatterns = [
    path('', views.airport_view, name='airport')
]
