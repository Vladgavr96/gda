from rest_framework import serializers
from flights.models import Passenger
from .flight_serializer import FlightSerializer


class PassengerSerializer(serializers.ModelSerializer):
    flights = FlightSerializer(many=True)

    class Meta:
        model = Passenger
        fields = ('__all__')
