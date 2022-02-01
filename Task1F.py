

from floodsystem.station import inconistant_typical_range_stations
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list

    test = inconistant_typical_range_stations(stations)

    print(test)

run()