
from .utils import sorted_by_key
from floodsystem.stationdata import *
from floodsystem.station import *


def stations_level_over_threshold(stations, tol):
    StationName = []
    StationLevel = []
    StationOver = []
    for station in stations:
        RelativeLevel = station.relative_water_level()
        if RelativeLevel is not None:
            if 200 > RelativeLevel > tol:
                StationName.append(station)
                StationLevel.append(station.relative_water_level())
                StationOver = list(zip(StationName, StationLevel))
    return sorted_by_key(StationOver, 1)


def stations_highest_rel_level(stations, N):
    StationInput =[]
    StationLevel = []
    StationList = []
    for station in stations:
        if station.relative_water_level() != None and station.relative_water_level() < 200:
            StationInput.append(station)
            StationLevel.append(station.relative_water_level())
            StationList = list(zip(StationInput,StationLevel))
    
    StationList.sort(key=lambda x:x[1], reverse = True)
    return[x[0] for x in StationList[:N]]


def station_above_max(stations):
    update_water_levels(stations)
    name = []
    levels = []
    for station in stations:
        if station.typical_range is not None:
            max = station.typical_range[1]
            latest_level = station.latest_level
            if latest_level is not None and latest_level < 50:
                if latest_level > max:
                    warning_level = latest_level - max
                    name.append(station.name)
                    levels.append(warning_level)
                else:
                    continue
            else:
                level = 0
                name.append(station.name)
                levels.append(level)
        else:
            continue

    danger = list(zip(name,levels))
    sorted_by_key(danger, 1, reverse = True)

    return danger
    


