
from tkinter import W
from floodsystem.stationdata import build_station_list
from floodsystem.station import *
from floodsystem.analysis import *
from floodsystem.flood import *
from floodsystem.datafetcher import *
import datetime

stations = build_station_list()

def run():
    DangerStations = station_above_max(stations)
    Warning_For_Stations = severity(DangerStations)

    print("**TOWNS CURRENTLY IN SEVERE DANGER OF FLOODING**\n")
    print(Warning_For_Stations[0])
    print("\n**TOWNS CURRENTLY IN MODERATE DANGER OF FLOODING**\n")
    print(Warning_For_Stations[1])
    print("\n**TOWNS CURRENTLY IN LOW DANGER OF FLOODING\n")
    print(Warning_For_Stations[2])

    future_station_name = []
    future_station_level = []
    dt = 10

    for station in stations[:50]:
        if station.typical_range is not None:
                dates, levels = datafetcher.fetch_measure_levels(station.measure_id, datetime.timedelta(days=dt))
                if dates is not [] and levels is not []:
                    future_level = future_levels(dates, levels, 4)
                    if station.typical_range is not None:
                        future_station_name.append(station.name)
                        future_station_level.append(future_level)

    station_future = list(zip(future_station_name,future_station_level))

    future_risk = severity(station_future)

    print ("**TOWNS PREDICTED TO BE IN SEVERE DANGER OF FLOODING IN 2 DASY**\n")
    print(future_risk[0])
    print("\n**TOWNS PREDICTED TO BE IN MODERATE DANGER OF FLOODING IN 2 DAYS**\n")
    print(future_risk[1])
    print("\n**TOWNS PREDICTED TO BE IN LOW DANGER OF FLOODING IN 2 DAYS\n")
    print(future_risk[2])



if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
