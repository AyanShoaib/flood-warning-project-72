from turtle import distance
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


def run():
    stations = build_station_list()
    p = (52.1805492, 0.1323424)
    d = stations_by_distance(stations, p)

    
    print("The closest 10 stations are:", d[:10])
    print ("The furthest 10 stations are:", d[-10:])


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()