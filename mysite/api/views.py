from rest_framework import viewsets
from flights.models import Flight, Passenger, Airport
from .serializers import FlightSerializer, PassengerSerializer, FeedbackSerializer, PassengerListSerializer, \
    AirportSerializer
from rest_framework.mixins import CreateModelMixin
from api.models import Feedback
from api.utils import query_debugger


class FlightViewset(viewsets.ModelViewSet):  # CRUD
    queryset = Flight.objects.all().select_related('origin', 'destination')  # prefetch_related для ManyToMany
    serializer_class = FlightSerializer

    @query_debugger
    def list(self, request, *args, **kwargs):
        print('Что-то что мы добавили')
        return super(FlightViewset, self).list(request, *args, **kwargs)


class PassengerViewset(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    http_method_names = ['get']

    def get_serializer_class(self):
        if self.action == 'list':
            return PassengerListSerializer
        return PassengerSerializer


class FeedbackViewset(viewsets.GenericViewSet, CreateModelMixin):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class AirportViewset(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
