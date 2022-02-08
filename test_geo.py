from floodsystem.stationdata import build_station_list
import floodsystem.geo as geo
from floodsystem.station import MonitoringStation
from haversine import haversine, Unit

def test_stations_by_distance():
    stations = build_station_list()
    centre=(0,0)
    StationDistance = geo.stations_by_distance(stations, centre)
    assert len(StationDistance) >0                                  #ensures that the distances are being added to the list
    for i in range (1, len(StationDistance)):
        assert StationDistance[i][2] >= StationDistance[i-1][2]     # As the fucntion requires the stations to be sorted from clostest to furthers, this test for every value that the ditnace in the next tuple is greater than the one before


def test_stations_within_radius():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    coord = (5.0,5.0)
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    coord = (10.0,10.0)
    s2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    coord = (180,0.0)
    s3 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    centre = (0.0,0.0)

    #Created 4 different stations with different distnaces, station S3 is built out of range of the radius to ensure on the stations within the radius r is added to the list, therefore only 3 stations should be in the list
    
    stations = [s,s1,s2,s3]
    r = haversine(centre, s2.coord, Unit.KILOMETERS) + 1
    WithinRadius = geo.stations_within_radius(stations, centre, r)
    assert len(WithinRadius) > 0
    assert len(WithinRadius) == 3
    
def test_river_with_station():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    river = "River Aire"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    river = "River Thames"
    s2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    stations = [s,s1,s2]
    rivers = geo.rivers_with_stations(stations)
    #Created a fake station list and checked if a river with a sation exits, the total length of the rivers with station is corresponding to the stations list and then whether the rivers exist in that list
    assert river is not None
    assert len(rivers) == 3
    assert "River Aire" in rivers
    assert "River Thames" in rivers
    
def test_stations_by_river():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "Station1"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    label = "Station2"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    label = "Station3"
    s2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    label = "Station4"
    s3 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    #Produced 4 stations that are allocted to one river, the function should add on 4 stations to the key - River X and the thus the length ofthe value to the key is 4
    stations = [s,s1,s2,s3]
    SBR = geo.stations_by_river(stations)

    assert len(SBR["River X"]) == 4
    

def test_rivers_by_station_number():
    stations = build_station_list()
    N = 3
    result = geo.rivers_by_station_number(stations, N)

    #using the database for the stations and N as 3 the lsit should have the top 4 rivers with the most stations

    assert len(result) == 4
    for i in range(1, len(result)):
        assert result[i][1] <= result[i-1][1]
    assert result[0][0] == "River Thames"

    #speciffically asserted river thames as its has the highest numbe rof stations and have signifcanlt more than any other station 
    #so it can be used a reliable river to test whether the list is sorted is descending order