from typing import Any
from django.core.management.base import BaseCommand

from station.utils import route_between_stations
from core.models import TrainHalts, Train
from station.models import StationRoute

class Command(BaseCommand):
    help = "Management command to load Train Route"

    def handle(self, *args: Any, **options: Any) -> str | None:

        TrainHalts.objects.all().delete()

        trains_queryset = Train.objects.all()

        for train in trains_queryset:
            source_station = StationRoute.objects.get(station__code=train.source_station_code)
            destination_station = StationRoute.objects.get(station__code=train.destination_station_code)
            routes = route_between_stations(source_station, destination_station)
            
            for halt in routes:
                TrainHalts.objects.create(train=train, halts=halt.station)

        print(f"Train Halts Created {TrainHalts.objects.count()}")