from station.models import Station
from core.models import TrainHalts, Train


def route_between_station_utils(source, destination, visited, route_list):
    if source == destination:
        return True
    
    for route in source.station.routes.all():
        if route not in visited:
            visited.append(route)
            if route_between_station_utils(route, destination, visited, route_list):
                route_list.append(route)
                return True
    
    return False

def route_between_stations(source, destination):
    route_list = []
    visited = [source]
    route_between_station_utils(source, destination, visited, route_list)
    route_list.append(source)
    route_list.reverse()
    return route_list


def train_between_two_stations(source, destination):
    src = Station.objects.get(code=source)
    dest = Station.objects.get(code=destination)
    source = TrainHalts.objects.filter(halts=src).values_list('train', flat=True)
    destination = TrainHalts.objects.filter(halts=dest).values_list('train', flat=True)
    stations = source.intersection(destination)
    trains = Train.objects.filter(pk__in=stations)
    filtered_trains = []
    for train in trains:
        train_route = list(TrainHalts.objects.filter(train=train).values_list('halts', flat=True))
        if train_route.index(src.id) < train_route.index(dest.id):
            filtered_trains.append(train)
    
    return filtered_trains
