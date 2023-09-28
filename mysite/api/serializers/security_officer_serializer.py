from rest_framework import serializers
from flights.models import SecurityOfficer
from .user_serializer import UserSerializer
from string import punctuation


class SecurityOfficerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    def validate_name(self, value):
        baned_symbols = list(punctuation)
        baned_symbols.extend(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])
        for i in value:
            if i in baned_symbols:
                raise serializers.ValidationError('Можно использовать только буквы')
        return value

    def validate_second_name(self, value):
        alphabet = 'йцукенгшщзхъфывапролдячсмитьб'
        for i in value:
            if i not in alphabet:
                raise serializers.ValidationError('Можно использовать только буквы')
        return value

    class Meta:
        model = SecurityOfficer
        fields = '__all__'
