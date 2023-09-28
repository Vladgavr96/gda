from flights.models import Airport, Flight
from rest_framework import serializers


class AirportSerializer(serializers.ModelSerializer):
    flights = serializers.SerializerMethodField()

    def get_flights(self, obj):
        from api.serializers import FlightShortSerializer
        flights = Flight.objects.filter(origin=obj)
        data = FlightShortSerializer(flights, many=True).data

        return data

    def validate_city(self, value):
        for i in value:
            if i.isnumeric():
                raise serializers.ValidationError('В названии города могут содержаться только буквы')
        return value

    def validate_name(self, value):
        print(value)
        return value.title()



    class Meta:
        model = Airport
        fields = ('name', 'city', 'flights')
