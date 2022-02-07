# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to

geographical data.

"""




from .utils import sorted_by_key 
from haversine import haversine, Unit


#Task 1B
def stations_by_distance(stations, p):
    distance = []
    StationName = []
    StationTown =[]
    for station in stations:
        if station.name:
            distance.append(haversine(station.coord,p,unit=Unit.KILOMETERS))
            StationName.append(station.name)
            StationTown.append(station.town)
    StationDistance = list(zip(StationName, StationTown, distance))
    StationDistance = sorted_by_key(StationDistance, 2)
    return StationDistance

#Task 1C
def stations_within_radius(stations, centre, r):
    WithinRadius =[]
    for station in stations:
        if haversine(centre, station.coord) < r:
            WithinRadius.append(station.name)
    WithinRadius = sorted_by_key(WithinRadius,0)
    return  WithinRadius
    



# Task 1D

def rivers_with_stations(stations):
    riverswithstation = set()
    for station in stations:
        if station.river:
            riverswithstation.add(station.river)
    return riverswithstation

def stations_by_river(stations):
    StationByRiver = {}
    for station in stations:
        if station.river in StationByRiver:
            StationByRiver[station.river].append(station.name)
            StationByRiver[station.river].sort()
        else:
            StationByRiver[station.river] = [station.name]
    return StationByRiver

# Task 1E
def rivers_by_station_number(stations, N):
    RiversByStationNumber = {}
    for station in stations:
        if station.river in RiversByStationNumber:
            RiversByStationNumber[station.river].append(station.name)
            len(RiversByStationNumber[station.river])
        else:
            RiversByStationNumber[station.river] = [station.name]
    p = []

    for key in RiversByStationNumber:
        p.append((key,len(RiversByStationNumber[key])))

    NumberOrder = sorted_by_key(p,1,reverse=True)
    FirstN = NumberOrder[0:N]

    return FirstN

    


  
    


        


