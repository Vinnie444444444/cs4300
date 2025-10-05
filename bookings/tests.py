from django.test import TestCase
from .models import Movie, Seat, Booking
from django.contrib.auth.models import User
from datetime import date

class MovieModelTest(TestCase):
    def test_create_movie(self):
        movie = Movie.objects.create(
            title="Test Movie",
            description="A test movie description.",
            release_date=date.today(),
            duration=120
        )
        self.assertEqual(movie.title, "Test Movie")
        self.assertTrue(isinstance(movie, Movie))
        self.assertEqual(str(movie), "Test Movie")

class SeatModelTest(TestCase):
    def test_create_seat(self):
        movie = Movie.objects.create(title="Inception", duration=120)
        seat = Seat.objects.create(seat_number="A1", is_booked=False, movie=movie)
        self.assertEqual(seat.seat_number, "A1")
        self.assertFalse(seat.is_booked)
        self.assertEqual(seat.movie.title, "Inception")

class BookingModelTest(TestCase):
    def test_create_booking(self):
        movie = Movie.objects.create(title="Avatar", duration=150)
        seat = Seat.objects.create(seat_number="B2", is_booked=False, movie=movie)
        booking = Booking.objects.create(movie=movie, seat=seat, user_name="John Doe")
        self.assertEqual(booking.user_name, "John Doe")
        self.assertEqual(booking.movie.title, "Avatar")
        self.assertEqual(booking.seat.seat_number, "B2")
