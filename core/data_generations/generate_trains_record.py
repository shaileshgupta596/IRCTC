import os
import json
import random
from django.conf import settings

express_train_types = [
    "Rajdhani Express",        # High-speed train connecting major cities
    "Shatabdi Express",        # Fast train for short to medium distances
    "Duronto Express",         # Non-stop express trains covering long distances
    "Superfast Express",       # Trains with fewer stops and faster speeds
    "Mail Express",            # Trains serving both passenger and freight purposes
    "Jan Shatabdi Express",    # Economical variant of Shatabdi Express
    "Garib Rath Express",      # Budget train service for economically weaker sections
    "August Kranti Express",   # Express trains commemorating the August Kranti movement
    "Sampark Kranti Express",  # Express trains connecting major cities with fewer stops
    "Tejas Express",           # Premium train offering modern amenities
    "Express",                 # General category for various express trains
    "Intercity Express",       # Express trains connecting neighboring cities
    "Double Decker Express",   # Express trains with double-decker coaches
    "Fast Passenger",          # Trains that are faster than ordinary passenger trains
    "Mail",                    # Mail trains serving mail and passenger needs
    "Economy Express"          # Budget-friendly express trains
]

def load_station_details():
    with open(f"{os.getcwd()}/core/data/IndianStation.json", 'r') as f:
        stations_data = json.load(f)

    all_station = [{'station_name': station.get('station_name'), 'station_code':station.get('station_code')} for station in stations_data]
    return all_station

def dump_train_details(all_train_details):
    with open(f"{os.getcwd()}/core/data/IndianTrains.json", 'w') as f:
        json.dump(all_train_details, f, indent=4)


def main():
    all_station = load_station_details()
    all_trains_dict = {}
    for i in range(200):
        source = random.choice(all_station)
        destination = random.choice(all_station)
        express_type = random.choice(express_train_types)
        
        if source.get('station_code') != destination.get('station_code'):
            train_name = f"{source.get('station_name')} -> {destination.get('station_name')} {express_type}"
            if not all_trains_dict.get(train_name):
                all_trains_dict[train_name] = {
                    'train_name': train_name,
                    'train_number': int(random.uniform(10000, 90000)),
                    'express_type': express_type,
                    'source_station' : source.get('station_name'),
                    'source_station_code': source.get('station_code'),
                    'destination_station' : destination.get('station_name'),
                    'destination_station_code': destination.get('station_code')
                }

    all_trains_list = list(all_trains_dict.values())
    dump_train_details(all_trains_list)
            
if __name__ == "__main__":
    main()
