from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from django.contrib.auth.decorators import login_required
def home(request):
    return HttpResponse("Welcome to the Movie Booking System!")
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})

@login_required
def book_seat(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = movie.seats.all()

    if request.method == 'POST':
        seat_id = request.POST.get('seat_id')
        seat = Seat.objects.get(id=seat_id)
        if not seat.is_booked:
            seat.is_booked = True
            seat.save()
            Booking.objects.create(movie=movie, seat=seat, user=request.user)
            return redirect('booking_history')

    return render(request, 'bookings/seat_booking.html', {'movie': movie, 'seats': seats})

@login_required
def booking_history(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})
