from django.urls import path
from .views import hello, flights, flight

urlpatterns = [
    #path('hello', hello),
    path('flights', flights),
    path('flights/<int:flight_id>', flight)
]