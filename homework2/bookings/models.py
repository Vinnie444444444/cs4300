from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField(default="2000-01-01")
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    description = models.TextField(default="Description not provided")

    def __str__(self):
        return self.title

class Seat(models.Model):
    seat_number = models.CharField(max_length=5)
    is_booked = models.BooleanField(default=False)
    movie = models.ForeignKey(Movie, related_name='seats', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.seat_number} - {self.movie.title}"

class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.movie.title} - {self.seat.seat_number}"

