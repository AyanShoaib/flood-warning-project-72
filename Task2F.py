import datetime
from distutils.command.build import build
from floodsystem.stationdata import update_water_levels, build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level

def run():
    stations = build_station_list()
    update_water_levels(stations)
    high_water_lev = stations_highest_rel_level(stations, 5)

    station_list = []
    for station in high_water_lev:
        station_list.append(station)
    
    for station in station_list:
        dt = 2
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days = dt))
        plot_water_level_with_fit(station, dates, levels, 4)


if __name__ == '__main__':
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()