from django.db import models
from django.utils.timezone import now


class Airport(models.Model):
    name = models.CharField(max_length=60, verbose_name='Название')
    city = models.CharField(max_length=60, verbose_name='Город')
    image = models.ImageField(verbose_name='Фото', blank=True, null=True)

    def __str__(self):
        return f'Аэропорт {self.name} в городе {self.city}'

    def get_arrivals(self):
        return self.flight_destination.all()

    class Meta:
        verbose_name = 'Аэропорт'
        verbose_name_plural = 'Аэропорты'
        ordering = ('city', )


class Flight(models.Model):
    origin = models.ForeignKey(Airport, verbose_name='Точка отправления', related_name='flight_origin',
                               on_delete=models.CASCADE, null=True)
    destination = models.ForeignKey(Airport, verbose_name='Точка прибытия', related_name='flight_destination',
                                    on_delete=models.CASCADE, null=True)
    duration = models.IntegerField(verbose_name='Длительность')
    created = models.DateTimeField(verbose_name='Время создания', default=now)

    def __str__(self):
        return f'Вылет из {self.origin} в {self.destination}. Длительность {self.duration} часов\n'

    class Meta:
        verbose_name = 'Вылет'
        verbose_name_plural = 'Вылеты'
        ordering = ('origin', 'duration')


class Passenger(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=60)
    second_name = models.CharField(verbose_name='Фамилия', max_length=60)
    flights = models.ManyToManyField(Flight, verbose_name='Вылеты', related_name='passanger_flights')
    slug = models.SlugField(verbose_name='ЧПУ', unique=True, blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.second_name}'
