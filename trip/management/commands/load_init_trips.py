from datetime import date, timedelta

from typing import Any
from django.core.management.base import BaseCommand
from django.db.models import Sum


from core.models import Train, TrainCoaches
from trip.models import TrainSeatAvailable


class Command(BaseCommand):
    help = "Load Initial Trips"

    def handle(self, *args: Any, **options: Any) -> str | None:
        TrainSeatAvailable.objects.all().delete()
        
        trains_qs = Train.objects.all()

        for train in trains_qs:
            seats_available = {}
            train_seats = TrainCoaches.objects.filter(train=train).values('type').annotate(seats=Sum('number_of_seats'))

            for object in train_seats:
                seats_available[object.get('type')] = object.get('seats')
           
            for day in range(30):
                TrainSeatAvailable.objects.create(
                    train=train,
                    seats=seats_available,
                    date=date.today() + timedelta(days=day)
                )
        
        print(f"Loaded Data for Trips for 1 Month for all trains {TrainSeatAvailable.objects.count()}")

