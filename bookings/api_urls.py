from rest_framework import routers
from .views import MovieViewSet, SeatViewSet, BookingViewSet
from django.urls import path, include
router = routers.DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

