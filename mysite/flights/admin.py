from django.contrib import admin
from .models import Flight, Airport, Passenger

# Register your models here.
admin.site.register(Flight)
admin.site.register(Passenger)


class FlightInline(admin.TabularInline):
    model = Flight
    fk_name = 'origin'
    extra = 10

@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
    inlines = [FlightInline, ]
