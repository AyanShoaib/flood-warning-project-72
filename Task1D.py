from ast import Return
from email import message
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_stations
from floodsystem.geo import stations_by_river



def riverswithstation_run():

    stations = build_station_list()

    print("There are {} rivers with stations, below are the first 10 in alphabetical arrangemnet".format(len(rivers_with_stations(stations))))

    sorted_rivers = sorted(rivers_with_stations(stations))

    print(sorted_rivers[:10])

def stationsbyriver_run():

    stations = build_station_list()

    SBR = stations_by_river(stations)

    River_Aire = SBR["River Aire"]
    River_Thames = SBR["River Thames"]
    River_Cam = SBR["River Cam"]

    message = "The stations with allocated rivers are, River Aire: {} River Thames: {} River Cam: {}".format(River_Aire, River_Thames, River_Cam)

    print(message)



if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    riverswithstation_run()
    stationsbyriver_run()

