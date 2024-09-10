from station.models import Station


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
