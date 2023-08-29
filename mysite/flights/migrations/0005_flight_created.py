# Generated by Django 4.2.4 on 2023-08-24 16:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0004_flight_destination_flight_origin'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время создания'),
        ),
    ]