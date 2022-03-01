from sympy import plot
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level

import datetime

def run():
    stations = build_station_list()
    update_water_levels(stations)
    high_water_lev = stations_highest_rel_level(stations, 5)

    dt = 10

    for station in high_water_lev:
        dates, level = fetch_measure_levels(station.measure_id, datetime.timedelta(days=dt))
        plot_water_levels(station, dates, level)

if __name__ == '__main__':
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()

