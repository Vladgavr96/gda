from flights.models import Flight
from rest_framework import serializers
from .airport_serializer import AirportSerializer

class FlightSerializer(serializers.ModelSerializer):
    origin = AirportSerializer() #В случае если модели связаны через ManyToMany то добавьте сюда many=True
    destination = AirportSerializer()

    class Meta:
        model = Flight
        fields = ('__all__')