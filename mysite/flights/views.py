from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Flight


# Create your views here.
def hello(request):
    return HttpResponse('hello')


def flights(request):
    f = Flight.objects.all()
    context = {
        'flights': f
    }
    return render(request, 'index.html', context)


def flight(request, flight_id):
    #f = Flight.objects.get(pk=flight_id)
    f = get_object_or_404(Flight, pk=flight_id)
    return HttpResponse(f)
