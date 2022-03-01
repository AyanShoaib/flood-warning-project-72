
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.flood import stations_highest_rel_level

def test_stattion_above_threshold():
    stations = build_station_list()
    stations_above_threshold = stations_level_over_threshold(stations, 1)
    for station in stations_above_threshold:
        assert station[1] > 1

def test_high_rel_levl():
    stations = build_station_list()
    update_water_levels(stations)
    
    flooded_stations = stations_highest_rel_level(stations, 50)
    assert len(flooded_stations) == 50
    