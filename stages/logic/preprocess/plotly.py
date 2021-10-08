"""
This file contains the logic to preprocess charts that are from plotly.
"""

from svgpathtools import parse_path
from stages.logic.preprocess.chart_sources import plotly as attributes
from supported_chart_types import SupportedType
from math import inf


def check_plotly_axes(soup):
    # from the dataset, it looks like there's only ever two axes
    x_axes = soup.find('g', class_="g-xtitle")
    y_axes = soup.find('g', class_="g-ytitle")

    if x_axes is not None and y_axes is not None:  # there are axes labels
        axes_labels = [x_axes.get_text(), y_axes.get_text()]
        if axes_labels.count('') == 0:  # we need at least 2 axes labelled
            return axes_labels

    return False


def check_plotly_title(soup):
    try:  # can't find the svg
        title = soup.find('svg').find('title')
    except Exception as e:
        return False

    if title is None or title == '':
        title = soup.find('g', class_='g-gtitle')
        if title is not None:
            return title.get_text()
    else:
        return title.get_text()

    return False


def get_paths(soup, graph_type, attributes):
    class_id = attributes[graph_type]
    paths = soup.find_all('g', class_=class_id)
    coords = []
    for i in range(len(paths)):
        if graph_type == 'line':
            path_string = paths[i].find('path')['d']
            coords.append(parse_path(path_string))
        elif graph_type == 'scatterplot':
            # get transform
            nested_paths = paths[i].find_all('path')
            for j in range(len(nested_paths)):
                try:
                    path_string = nested_paths[j]['transform']
                    x, y = path_string[10:].split(',')
                    coords.append((float(x),float(y[:-1])))
                except:
                    continue
        elif graph_type == 'bar':
            nested_paths = paths[i].find_all('path')
            for j in range(len(nested_paths)):
                path_string = nested_paths[j]['d']
                coords.append(parse_path(path_string))

    return coords


def get_axes_ticks(soup, attributes):
    x_axes_ticks_id = attributes['x_axis_ticks']
    axes = soup.find_all('g', class_=x_axes_ticks_id)
    x_labels = []
    x_coords = []

    for i in range(len(axes)):
        labels = axes[i].find_all('text')

        for j in range(len(labels)):
            x_labels.append(labels[j].get_text())
        x_coords.append(axes[i].find('text')['transform'])

    for i in range(len(x_coords)):
        x_coords[i] = float(x_coords[i][10:].split(',')[0])  # only keep y value

    y_labels = []
    y_axes_ticks_id = attributes['y_axis_ticks']
    y_coords = []

    if x_axes_ticks_id == y_axes_ticks_id:  # same class is used for x and y axes ticks
        axes = axes[1].find_all('text')
    else:  # different class is used
        axes = soup.find_all('g', class_=y_axes_ticks_id)

    for i in range(len(axes)):
        labels = axes[i].find_all('text')

        for j in range(len(labels)):
            y_labels.append(labels[j].get_text())
        y_coords.append(axes[i].find('text')['transform'])
    for i in range(len(y_coords)):
        y_coords[i] = float(y_coords[i].split(',')[1][:-1])  # only keep x value

    return x_labels, x_coords, y_labels, y_coords


def calculate_y_data_point(coord, labels, axes_coords):
    left_label = None
    right_label = None
    for i in range(len(axes_coords)-1):
        right = axes_coords[i]
        left = axes_coords[i+1]
        if left <= coord <= right:
            # the value is in between these axes labels
            right_label = float(labels[i].replace('−','-').replace(',',''))
            left_label = float(labels[i+1].replace('−','-').replace(',',''))
            break
    if left_label is None:
        return -inf

    interval = right - left
    dist = coord - left
    actual_value = left_label + (dist/interval * (right_label - left_label))

    return actual_value


def convert_path_to_data(x_labels, x_coords, y_labels, y_coords, lines, graph_type, height):
    if graph_type == 'scatterplot':
        for i in range(len(lines)):
            x, y = lines[i]
            y = height - lines[i][1]
            lines[i] = (x, y)
        return lines

    line_data_points = []
    if graph_type == 'line':
        for i in range(len(lines)):
            current_line = lines[i]
            for j in range(len(current_line)):
                coord = current_line[j]
                x = coord.start.real
                y = height - coord.start.imag
                line_data_points.append((x, y))

    if graph_type == 'bar':
        category_counter = 0
        invalid_categories = []
        for i in range(len(lines)):
            current_line = lines[i]
            # check the x coords of first and last points of the bar to see if label lies between
            start = current_line[0].start.real
            end = current_line[len(current_line)-1].start.real
            y = current_line[1].start.imag
            x_value = None
            y_value = None

            for j in range(category_counter,len(x_coords)):
                x = x_coords[j]
                if start <= x <= end:
                    x_value = x_labels[j]
                    y_value = calculate_y_data_point(y, y_labels, y_coords)
                    category_counter += 1
                    break

            if y_value != -inf:
                line_data_points.append((x_value, y_value))
            else:
                invalid_categories.append(x_value)  # value could not be retrieved

        if len(x_labels) != len(line_data_points):  # we didn't retrieve all the bars
            for i in range(len(x_labels)):  # sometimes y value of 0 doesn't show up as bars
                if x_labels[i] not in invalid_categories:
                    found = False
                    for j in range(len(line_data_points)):
                        if line_data_points[j][0] == x_labels[i]:
                            found = True
                            break
                    if not found:
                        line_data_points.append((x_labels[i], 0))

    return line_data_points


def read_plotly_chart(soup, graph_type):
    if graph_type == SupportedType.LINE:
        graph_type = 'line'
    elif graph_type == SupportedType.SCATTER:
        graph_type = 'scatterplot'
    elif graph_type == SupportedType.BAR:
        graph_type = 'bar'

    axes_labels = check_plotly_axes(soup)
    title_text = check_plotly_title(soup)
    lines = get_paths(soup, graph_type, attributes)
    x_labels, x_coords, y_labels, y_coords = get_axes_ticks(soup, attributes)
    height = float(soup.find('svg')['height'])
    data_points = convert_path_to_data(x_labels, x_coords, y_labels, y_coords, lines, graph_type, height)

    if axes_labels and title_text:
        info = {
            "title": title_text,
            "x_axis_title": axes_labels[0],
            "y_axis_title": axes_labels[1],
            "x_tick_labels": x_labels,
            "y_tick_labels": y_labels,
            "data": data_points
        }
        return info  # valid chart

    return False  # invalid chart