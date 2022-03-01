from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels


def run():

    stations = build_station_list()
    update_water_levels(stations)
    stations_level_over_threshold_list = stations_level_over_threshold(stations, 0.8)
    for (station, level) in stations_level_over_threshold_list:
        print(station.name," ",level)

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()