from django.db import models


# Create your models here.
class Flight(models.Model):
    origin = models.CharField(max_length=256, verbose_name='Точка отправления')
    destination = models.CharField(max_length=256, verbose_name='Точка прибытия')
    duration = models.IntegerField(verbose_name='Длительность')

    def __str__(self):
        return f'Вылет из {self.origin} в {self.destination}. Длительность {self.duration} часов'
