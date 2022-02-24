from floodsystem.station import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.utils import sorted_by_key

def run():

    stations = build_station_list()

    return stations_level_over_threshold(stations, 0.8)
