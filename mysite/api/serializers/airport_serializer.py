from flights.models import Airport, Flight
from rest_framework import serializers


class AirportSerializer(serializers.ModelSerializer):
    flights = serializers.SerializerMethodField()

    def get_flights(self, obj):
        from api.serializers import FlightShortSerializer
        flights = Flight.objects.filter(origin=obj)
        data = FlightShortSerializer(flights, many=True).data

        return data



    class Meta:
        model = Airport
        fields = ('name', 'city', 'flights')
