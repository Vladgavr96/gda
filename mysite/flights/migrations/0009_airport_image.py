# Generated by Django 4.2.5 on 2023-09-14 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0008_passenger_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='airport',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото'),
        ),
    ]