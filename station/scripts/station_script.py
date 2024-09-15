from django.db.models import Q

from station.models import Station, StationRoute
from core.models import TrainHalts, Train

from station.utils import route_between_stations



def run():
    src = Station.objects.get(code='AGC')
    dest = Station.objects.get(code='NDLS')
    source = TrainHalts.objects.filter(halts=src).values_list('train', flat=True)
    destination = TrainHalts.objects.filter(halts=dest).values_list('train', flat=True)
    stations = source.intersection(destination)
    trains = Train.objects.filter(pk__in=stations)
    filtered_trains = []
    for train in trains:
        train_route = list(TrainHalts.objects.filter(train=train).values_list('halts', flat=True))
        if train_route.index(src.id) < train_route.index(dest.id):
            filtered_trains.append(train)
    
    print(filtered_trains)
        
        



