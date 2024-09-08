from station.models import Station, StationRoute

def run():
    kalyan = StationRoute.objects.get(station__code="KYN")
    print(kalyan.routes.all())



