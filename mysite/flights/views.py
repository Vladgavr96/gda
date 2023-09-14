from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Flight, Airport, Passenger


# Create your views here.
def hello(request):
    #all_objs = Flight.objects.all()[1:3]
    #first_obj = Flight.objects.first()
    #ordered_obj = Flight.objects.order_by('-duration') сортировка по длительности
    #longest_obj = Flight.objects.order_by('-duration').first()
    #get_obj = Flight.objects.get(id=1)

    #my_airport = Airport.objects.get(name='Пулково')
    #get_airports_flights = Flight.objects.filter(destination=my_airport) #тут можно вместо объекта аэропорта использовать его id

    #get_exclude_airports = Flight.objects.filter(origin=2).exclude(destination=1)
    #print(get_exclude_airports.first())

    #my_airport1 = Airport.objects.get(name='Пулково')
    #my_airport2 = Airport.objects.get(name='Хитроу')
    #f = Flight.objects.create(origin=my_airport1, destination=my_airport2, duration=2)
    #print(f)

    #f = Flight.objects.get(id=1)
    #f.duration = 200
    #f.save()

    #Flight.objects.get(id=1).delete()
    """Airport.objects.bulk_create([
        Airport(name='Иваново', city='Иваново'),
        Airport(name='Внуково', city='Москва')
    ])"""

    #print(Airport.objects.get_or_create(name='Домодедово', city='Москва'))
    my_airport = Airport.objects.get(name='Шереметьево')
    res = Passenger.objects.filter(flights__origin=my_airport)[:3]

    return HttpResponse(res)


def airports(request):
    f = Airport.objects.all()
    context = {
        'airports': f
    }
    return render(request, 'index.html', context)


def flight(request, flight_id):
    # f = Flight.objects.get(pk=flight_id)
    f = get_object_or_404(Flight, pk=flight_id)
    context = {
        'flight': f,
        'passangers': f.passanger_flights.all()
    }
    return render(request, 'flight.html', context)


def date_filter(request):
    start_date = request.GET.get('start_date')
    filter_type = request.GET.get('filter_type')
    f = None
    if start_date:
        if filter_type == 'gte':
            f = Flight.objects.filter(created__gte=start_date)
        elif filter_type == 'lte':
            f = Flight.objects.filter(created__lte=start_date)
    context = {
        'flights': f,
        'date': start_date,
        'filter_type':filter_type
    }
    return render(request, 'date_filter.html', context)

def passanger(request, slug):
    p = Passenger.objects.get(slug=slug)

    context = {
        'passanger' : p
    }
    return HttpResponse(p)