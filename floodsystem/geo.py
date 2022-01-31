# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""


from xmlrpc.server import SimpleXMLRPCRequestHandler
from floodsystem.stationdata import build_station_list
from .utils import sorted_by_key  # noqa

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