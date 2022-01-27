# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""


from xmlrpc.server import SimpleXMLRPCRequestHandler
from floodsystem.stationdata import build_station_list
from .utils import sorted_by_key  # noqa


def stations_by_rivers(stations):
    stationsByRivername = {}

    rivername = input("Enter River: ")
    for station in stations:
        if station.river in [ rivername ]:
            if station.river in stationsByRivername:
                stationsByRivername[station.river].append(station.name)
            else:
                stationsByRivername[station.river] = []
    return stationsByRivername

def rivers_with_stations(stations):
    riverswithstation = set()
    for station in stations:
        if station.river:
            riverswithstation.add(station.river)
    return riverswithstation

