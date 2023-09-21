from rest_framework import routers
from .views import FlightViewset, PassengerViewset, FeedbackViewset, AirportViewset

flight_router = routers.DefaultRouter()
flight_router.register('flights', FlightViewset)
flight_router.register('passengers', PassengerViewset)
flight_router.register('feedback', FeedbackViewset)
flight_router.register('airport', AirportViewset)


urlpatterns = []
urlpatterns += flight_router.urls