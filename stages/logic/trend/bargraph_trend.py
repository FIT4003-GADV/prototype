"""
Trend finder logic for bar graphs. Returns the max/min category and values.
"""


def trend_bar(info):

    bar_tuple = info['data']
    max_data = max(bar_tuple,key=lambda item:item[1])
    min_data = min(bar_tuple,key=lambda item:item[1])

    # max_string = "Highest value is "+ str(max_data[0])+ " " + str(max_data[1]) + "\n"
    # min_string = "Lowest value is " + str(min_data[0]) + " " + str(min_data[1])

    return max_data, min_data
