import datetime
from floodsystem.stationdata import update_water_levels, build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit

def run():
    stations = build_station_list()
    update_water_levels(stations)

    station_list = []
    for station in stations:
        station_list.append(station)
    
    for station in station_list:
        dt = 2
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days = dt))
        plot_water_level_with_fit(station, dates, levels, 4)


if __name__ == '__main__':
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()