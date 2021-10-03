"""
Trend finder for line and scatterplots using linear regression.
Returns 1 = increasing, 2 = decreasing, 3 = flat.
"""
import numpy as np
from sklearn.linear_model import LinearRegression


def trend_generator(info):
    data_tuple = info['data']

    xarr = []
    yarr = []

    for tuple in data_tuple:
        xarr.append(tuple[0])
        yarr.append(tuple[1])

    x = np.array(xarr).reshape((-1, 1))
    y = np.array(yarr)

    model = LinearRegression().fit(x, y)

    slope = model.coef_[0]

    if slope > 0:
        return 1
    elif slope < 0:
        return 2
    else:
        return 3
