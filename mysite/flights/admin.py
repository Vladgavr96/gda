from django.contrib import admin
from .models import Flight, Airport

# Register your models here.
admin.site.register(Flight)


class FlightInline(admin.TabularInline):
    model = Flight
    fk_name = 'origin'
    extra = 10

@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
    inlines = [FlightInline, ]
