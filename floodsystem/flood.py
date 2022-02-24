
from .utils import sorted_by_key


def stations_level_over_threshold(stations, tol):
    StationName = []
    StationLevel = []
    StationOver = []
    for station in stations:
        RelativeLevel = station.relative_water_level()
        if RelativeLevel is not None :
            if RelativeLevel > tol:
                StationName.append(station.name)
                StationLevel.append(station.relative_water_level())
                StationOver = list(zip(StationName, StationLevel))
    return sorted_by_key(StationOver, 1)