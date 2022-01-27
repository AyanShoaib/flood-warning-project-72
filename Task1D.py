from ast import Return
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_stations, stations_by_rivers


def stationbyrivers_run():
    """Requirements for Task 1A"""

    # Build list of stations
    stations = build_station_list()

    sorted_stations = sorted(stations_by_rivers(stations))

    print(sorted_stations)

def riverswithstation_run():

    stations = build_station_list()

    print("Stations: {}".format(len(rivers_with_stations(stations))))

    sorted_rivers = sorted(rivers_with_stations(stations))

    print(sorted_rivers)


if __name__ == "__main__":
   stationbyrivers_run()
   riverswithstation_run()
