from django.urls import path
from .views import hello, airports, flight

urlpatterns = [
    # path('hello', hello),
    path('', airports),
    path('<int:flight_id>', flight, name='flight')
]
