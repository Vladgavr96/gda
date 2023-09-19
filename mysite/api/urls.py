from rest_framework import routers
from .views import FlightViewset, PassengerViewset, FeedbackViewset

flight_router = routers.DefaultRouter()
flight_router.register('flights', FlightViewset)
flight_router.register('passengers', PassengerViewset)
flight_router.register('feedback', FeedbackViewset)


urlpatterns = []
urlpatterns += flight_router.urls