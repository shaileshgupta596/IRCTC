import json
from typing import Any
from django.core.management.base import BaseCommand
from django.conf import settings


from station.models import Station, StationRoute



class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> str | None:
        StationRoute.objects.all().delete()

        with open(settings.BASE_DIR /"station/data/routes.json", 'r') as f:
            routes_data = json.load(f)
            for route in routes_data:
                station = Station.objects.get(code=route.get('code'))
                route_object = StationRoute(station=station)
                route_object.save()
                connected_routes = route.get('backward_stations') + route.get('forward_stations')
                connected_routes = Station.objects.filter(code__in=connected_routes).values_list('id', flat=True)
                route_object.routes.add(*list(connected_routes))
        
        print(F"Created Routes for {StationRoute.objects.count()} stations.")