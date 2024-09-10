from django.db.models import Q

from station.models import Station, StationRoute
from core.models import TrainHalts



def run():
    src = Station.objects.get(code='KYN')
    dest = Station.objects.get(code='BSL')
    src_halts = TrainHalts.objects.filter(halts=src)
    dest_halts = TrainHalts.objects.filter(halts=dest)
    print(src_halts, dest_halts)
    print(src_halts.intersection(dest_halts))

    # print(StationRoute.objects.get(station__code='BSL').routes.all())



