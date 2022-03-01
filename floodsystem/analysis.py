from http.client import ImproperConnectionState
import matplotlib
import numpy as np
import datetime


def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    d0 = x[0]
    x-= d0
    y = levels

    p_coeff = np.polyfit(x, y, p)
    poly = np.poly1d(p_coeff)

    return poly, d0

def severity(stations):
    severe = []
    moderate = []
    low = []
    none = []

    for danger in stations:
        if 1.0 > danger[1] > 0.5 or danger[1] == 0.5:
            low.append(danger[0])
        if 1.5 > danger[1] > 1.0 or danger[1] == 1.0:
            moderate.append(danger[0])
        if danger[1] > 1.5 or danger[1] == 1.5:
            severe.append(danger[0])
        if danger[1] < 0.5:
            none.append(danger[0])
        else:
            continue
    return severe, moderate, low, none

def future_levels(dates, level, p):
    date = matplotlib.dates.date2num(dates)
    try:
        p_coeff = np.polyfit(date - date[0],level,p)
    except:
        p_coeff = 0
    poly = np.poly1d(p_coeff)

    test_date = matplotlib.dates.date2num(datetime.datetime.now() + datetime.timedelta(days = 2))

    return(poly(test_date - date[0]))