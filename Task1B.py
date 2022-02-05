from turtle import distance
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


def run():
    stations = build_station_list
    p = (52.1805492, 0.1323424)
    distance = stations_by_distance(stations, p)

    
    print("Closest Stations: ", distance[:10])
    print("Furthest Stations: ", distance[:-10])


if __name__ == "__main__":
    run()