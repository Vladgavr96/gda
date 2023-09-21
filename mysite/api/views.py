from rest_framework import viewsets
from flights.models import Flight, Passenger
from .serializers import FlightSerializer, PassengerSerializer, FeedbackSerializer, PassengerListSerializer
from rest_framework.mixins import CreateModelMixin
from api.models import Feedback



class FlightViewset(viewsets.ModelViewSet): #CRUD
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class PassengerViewset(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    http_method_names = ['get']

    def get_serializer_class(self):
        print(self.action)
        if self.action == 'list':
            return PassengerListSerializer
        return PassengerSerializer

class FeedbackViewset(viewsets.GenericViewSet, CreateModelMixin):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
