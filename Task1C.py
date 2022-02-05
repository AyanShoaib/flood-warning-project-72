
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list
    StationNearCambridge = stations_within_radius(stations, (52.2053,0.1218), 10)
    print(StationNearCambridge)

if __name__ == "__main__":
    run()