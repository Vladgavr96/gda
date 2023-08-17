from django.urls import path
from .views import hello, flights

urlpatterns = [
    path('hello', hello),
    path('flights', flights),
]