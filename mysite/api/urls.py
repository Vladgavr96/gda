from rest_framework import routers
from .views import FlightViewset

flight_router = routers.DefaultRouter()
flight_router.register('flights', FlightViewset)


urlpatterns = []
urlpatterns += flight_router.urls