import matplotlib
import numpy as np


def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    d0 = x[0]
    x-= d0
    y = levels

    p_coeff = np.polyfit(x, y, p)
    poly = np.poly1d(p_coeff)

    return poly, d0