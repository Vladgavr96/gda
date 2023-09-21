from flights.models import Flight, Passenger
from rest_framework import serializers
from .airport_serializer import AirportSerializer


class FlightSerializer(serializers.ModelSerializer):
    origin = AirportSerializer() #В случае если модели связаны через ManyToMany то добавьте сюда many=True
    destination = AirportSerializer()
    passengers = serializers.SerializerMethodField()

    def get_passengers(self, obj):
        from api.serializers import PassengerSerializer
        #passengers = Passenger.objects.filter(flights=obj)

        passengers = obj.passanger_flights.all()

        #data = PassengerSerializer(passengers, many=True)
        #print(data)
        return 1

    class Meta:
        model = Flight
        fields = ('__all__')