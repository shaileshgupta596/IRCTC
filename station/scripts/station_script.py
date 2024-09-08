from station.models import Station, StationRoute

def route_between_station(source, destination, visited, route_list):
    if source == destination:
        return True
    
    for route in source.station.routes.all():
        if route not in visited:
            visited.append(route)
            if route_between_station(route, destination, visited, route_list):
                route_list.append(route)
                return True
    
    return False


def run():
    source = StationRoute.objects.get(station__code='CSMT')
    destination = StationRoute.objects.get(station__code='AGC')
    route_list = []
    visited = [source]
    print(route_between_station(source, destination, visited, route_list))
    print(route_list)

    # print(StationRoute.objects.get(station__code='BSL').routes.all())



