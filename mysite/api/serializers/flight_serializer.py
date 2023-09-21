from flights.models import Flight, Passenger
from rest_framework import serializers
from .airport_serializer import AirportSerializer


class FlightSerializer(serializers.ModelSerializer):
    origin = AirportSerializer() #В случае если модели связаны через ManyToMany то добавьте сюда many=True
    destination = AirportSerializer()
    passengers = serializers.SerializerMethodField()

    def get_passengers(self, obj):
        from api.serializers import PassengerListSerializer
        passengers = Passenger.objects.filter(flights=obj)
        #passengers = instance.passanger_flights.all()

        data = PassengerListSerializer(passengers, many=True).data
        return data

    class Meta:
        model = Flight
        fields = ('__all__')

class FlightShortSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        return str(obj)

    class Meta:
        model = Flight
        fields = ('name', )