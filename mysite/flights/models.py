from django.db import models
from django.utils.timezone import now


class Airport(models.Model):
    name = models.CharField(max_length=60, verbose_name='Название')
    city = models.CharField(max_length=60, verbose_name='Город')

    def __str__(self):
        return f'Аэропорт {self.name} в городе {self.city}'

    def get_arrivals(self):
        return self.flight_destination.all()


class Flight(models.Model):
    origin = models.ForeignKey(Airport, verbose_name='Точка отправления', related_name='flight_origin', on_delete=models.CASCADE, null=True)
    destination = models.ForeignKey(Airport, verbose_name='Точка прибытия', related_name='flight_destination', on_delete=models.CASCADE, null=True)
    duration = models.IntegerField(verbose_name='Длительность')
    created = models.DateTimeField(verbose_name='Время создания', default=now)

    def __str__(self):
        return f'Вылет из {self.origin} в {self.destination}. Длительность {self.duration} часов\n'
