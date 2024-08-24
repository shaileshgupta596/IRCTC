from typing import Any
from django.core.management.base import BaseCommand
import requests
import json
from django.conf import settings

from core.models import Station, Train

class Command(BaseCommand):
    help = "Load Data in Backend"

    def handle(self, *args: Any, **options: Any) -> str | None:
        # Cleanup Activity for Stations
        Station.objects.all().delete()

        with open(settings.BASE_DIR /"core/data/IndianStation.json", 'r') as f:
            stations_data = json.load(f)
            all_station_instance = []
            for station_rec in stations_data:
                try:
                    all_station_instance.append(Station(
                        name = station_rec.get('station_name'),
                        code = station_rec.get('station_code'),
                        number_of_platforms = station_rec.get('number_of_platforms'),
                        type = station_rec.get('station_type'),
                        state = station_rec.get('state_code'),
                        zone = station_rec.get('zone_code') 
                    ))
                except Exception as e:
                    print(e)

            Station.objects.bulk_create(all_station_instance)
            print(f'Inserted {Station.objects.all().count()} Stations.')
        

        # Cleanup Activity for Stations
        Train.objects.all().delete()

        with open(settings.BASE_DIR /"core/data/IndianTrains.json", 'r') as f:
            trains_data = json.load(f)
            all_train_instance = []
            for train_rec in trains_data:
                try:
                    all_train_instance.append(Train(
                        name = train_rec.get('train_name'),
                        number = train_rec.get('train_number'),
                        source = train_rec.get('source_station'),
                        source_station_code = train_rec.get('source_station_code'),
                        destination = train_rec.get('destination_station'),
                        destination_station_code = train_rec.get('destination_station_code')
                    ))
                    
                except Exception as e:
                    print(e)

            Train.objects.bulk_create(all_train_instance)
            print(f'Inserted {Train.objects.all().count()} Trains.')