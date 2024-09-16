from django.db import models
from django.utils import timezone
from datetime import date, timedelta
from django.core.exceptions import ValidationError
from core.models import Train, TrainCoaches

# Create your models here.

def validated_date(trip_date):
    
    if trip_date >= date.today():
        raise ValidationError("Selected Past Date. Booking not available.")
    elif date.today() + timedelta(days=120)  < trip_date:
        raise ValidationError("Booking Not Available for selected Date.") 

class TrainSeatAvailable(models.Model):
    train = models.ForeignKey(Train, on_delete=models.SET_NULL, null=True,  related_name="train_seats_available")
    seats = models.JSONField()
    date = models.DateField(validators=[validated_date])

    def __str__(self) -> str:
        return f"{self.train.name} -> {self.date}"
