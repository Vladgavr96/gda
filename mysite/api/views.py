from rest_framework import viewsets
from flights.models import Flight, Passenger, Airport, SecurityOfficer
from .serializers import FlightSerializer, PassengerSerializer, FeedbackSerializer, PassengerListSerializer, \
    AirportSerializer, SecurityOfficerSerializer
from rest_framework.mixins import CreateModelMixin
from api.models import Feedback
from api.utils import query_debugger
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter


class FlightViewset(viewsets.ModelViewSet):  # CRUD
    queryset = Flight.objects.all().select_related('origin', 'destination')  # prefetch_related для ManyToMany
    serializer_class = FlightSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['origin', 'destination__name']
    ordering_fields = ['duration', 'created']
    search_fields = ['origin__name', 'destination__name']



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

class SecurityOfficerViewset(viewsets.ModelViewSet):
    queryset = SecurityOfficer.objects.all()
    serializer_class = SecurityOfficerSerializer

    def create(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super(SecurityOfficerViewset, self).create(request, *args, **kwargs)
        else:
            return Response('Доступно только админу')
