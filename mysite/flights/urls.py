from django.urls import path
from .views import hello, airports, flight, date_filter, passanger


app_name = 'flights'
urlpatterns = [
    path('hello', hello),
    path('', airports, name='airports'),
    path('<int:flight_id>', flight, name='flight'),
    path('passanger/<str:slug>', passanger, name='passanger'),
    path('date-filter/', date_filter, name='date_filter')
]
