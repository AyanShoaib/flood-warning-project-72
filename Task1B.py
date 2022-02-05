from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


def run():
    stations = build_station_list
    p = (52.1805492, 0.1323424)
    test = stations_by_distance(stations, p)
    
    print(test)


if __name__ == "__main__":
    run()