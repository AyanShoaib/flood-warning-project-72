# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to

geographical data.

"""


from tokenize import Number

from xmlrpc.server import SimpleXMLRPCRequestHandler

from .utils import sorted_by_key  # noqa
<<<<<<< HEAD
from haversine import haversine
=======
from haversine import haversine 
>>>>>>> 55116753f3f568bbb0c4b9d85ffb053ae553d2a4

#Task 1B
def stations_by_distance(stations, p):
    distance =[]
    stationname =[]
    for station in stations:
        if station.name:
            distance.append(haversine(p, station.coord))
            stationname.append(station.name)
    StationDistance =(list(zip(stationname, distance)))
    StationDistance = sorted_by_key(StationDistance, 1)
    return StationDistance
    



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
    NumberOrder = sorted(p, key=lambda x:x[1], reverse=True)
    FirstN = NumberOrder[0:N]
    return FirstN


  
    


        


