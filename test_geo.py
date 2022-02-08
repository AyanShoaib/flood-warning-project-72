from floodsystem.stationdata import build_station_list
import floodsystem.geo as geo
from floodsystem.station import MonitoringStation
from haversine import haversine, Unit

def test_stations_by_distance():
    stations = build_station_list()
    centre=(0,0)
    StationDistance = geo.stations_by_distance(stations, centre)
    assert len(StationDistance) >0
    for i in range (1, len(StationDistance)):
        assert StationDistance[i][2] >= StationDistance[i-1][2]


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

    assert river is not None
    assert len(rivers) == 3
    assert "River Aire" in rivers
    assert "River Thames" in rivers
    
def test_stations_by_river():
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
    river = "River Cam"
    s3 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    stations = [s,s1,s2,s3]
    SBR = geo.stations_by_river(stations)

    assert len(SBR["River Aire"]) == 1
    assert len(SBR["River Thames"]) == 1
    assert len(SBR["River Cam"]) == 1

def test_rivers_by_station_number():
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
    river = "River Cam"
    s3 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    stations = [s,s1,s2,s3]
    N = 3
    result = geo.rivers_by_station_number(stations, N)

    assert len(result) == 4
    for i in range(1, len(result)):
        assert result[i][1] >= result[i-1][1]
