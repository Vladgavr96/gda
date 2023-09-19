from rest_framework import viewsets
from flights.models import Flight
from .serializers import FlightSerializer



class FlightViewset(viewsets.ModelViewSet): #CRUD
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer