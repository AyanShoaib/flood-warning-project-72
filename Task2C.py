from Task2B import run
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels

def run():

    stations = build_station_list()
    update_water_levels(stations)
    stations_highest_rel_level_list = stations_highest_rel_level(stations, 10)
    for i in stations_highest_rel_level_list:
        print(i[0].name+" "+str(i[1]))



if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()