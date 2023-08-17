from django.shortcuts import render
from django.http import HttpResponse
from .models import Flight


# Create your views here.
def hello(request):
    return HttpResponse('hello')


def flights(request):
    f = Flight.objects.all()
    return HttpResponse(f)
