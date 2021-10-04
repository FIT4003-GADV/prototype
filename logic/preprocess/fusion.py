from supported_chart_types import SupportedType
import re


def check_fusion_x_axis_values(soup):
    pat = re.compile("(.*-dataset-Label-group)")
    labelGroup = soup.find_all('g', class_=pat)
    dataAxis = labelGroup[0].find_all('text')

    if labelGroup is not None:
        x_axis_values = []
        try:
            dataAxis = labelGroup[0].find_all('text')
            for i in range(len(dataAxis)):
                x_axis_values.append(dataAxis[i].get_text())
        except Exception as e:
            return False

        return ', '.join(x_axis_values)  # return a string for consistency
    return False


def check_fusion_y_axis_values(soup):
    pat = re.compile("(.*-dataset-Name-group)")
    axes = soup.find_all('g', class_=pat)

    if axes is not None:
        y_axis_values = []
        try:
            text = axes[0].find_all('text')
            for i in text:
                y_axis_values.append(i.get_text())
        except Exception as e:
            return False
        y_axis_values = y_axis_values[2:]
        return ', '.join(y_axis_values)  # return a string for consistency
    return False


def get_data_scatter_chart(soup):  # from coordinates data
    pat_canvas = re.compile("(.*-canvas)")
    canvas = soup.find('g', class_=pat_canvas)
    height = 0
    if canvas:
        # should be 1 item in canvas only, not sure why cannot use canvas[0]
        for item in canvas:
            try:
                height = item.attrs['height']
            except Exception as e:
                pass

    pat_anchors = re.compile("(.*-anchors)")
    anchors = soup.find('g', class_=pat_anchors)
    if anchors:
        # should be 1 item in canvas only, not sure why cannot use canvas[0]
        dataPoints = []
        for item in anchors:
            try:
                d = item.attrs['d']
                d_list = d.split(",")
                x_coord = float(d_list[0][1:])
                y_coord = float(d_list[1].partition("L")[0])

                if not (x_coord == 0 and y_coord == 0):
                    dataPoints.append((x_coord, float(height) - y_coord))
            except Exception as e:
                pass

        return dataPoints


def get_data_line_chart(soup):  # from coordinates data
    pat_canvas = re.compile("(.*-canvas)")
    canvas = soup.find('g', class_=pat_canvas)
    height = 0
    if canvas:
        # should be 1 item in canvas only, not sure why cannot use canvas[0]
        for item in canvas:
            try:
                height = item.attrs['height']
            except Exception as e:
                pass

    pat_anchors = re.compile("(.*-anchors)")
    anchors = soup.find('g', class_=pat_anchors)
    if anchors:
        # should be 1 item in canvas only, not sure why cannot use canvas[0]
        dataPoints = []
        for item in anchors:
            try:
                d = item.attrs['d']
                d_list = d.split(",")
                x_coord = float(d_list[0][1:])
                y_coord = float(d_list[1].partition("A")[0])

                if not (x_coord == 0 and y_coord == 0):
                    dataPoints.append((x_coord, float(height) - y_coord))
            except Exception as e:
                pass

        return dataPoints


def get_data_bar_chart(soup):  # actual y-axis value
    pat_datalabel = re.compile("(.*-datalabel)")
    data_labels = soup.find('g', class_=pat_datalabel)
    dataValue = []
    if data_labels is not None:  # get the data from the labels on the chart directly
        for value in data_labels:
            for text in value:
                try:
                    if len(text) > 0:
                        dataValue.append(text.get_text())
                except Exception as e:
                    pass
        return dataValue  # not all charts contain data label on the chart

    else:  # get data from coordinates data
        pat_canvas = re.compile("(.*-canvas)")
        canvas = soup.find('g', class_=pat_canvas)
        height = 0
        dataValue = []
        if canvas:
            # should be 1 item in canvas only, not sure why cannot use canvas[0]
            for item in canvas:
                try:
                    height = item.attrs['height']
                except Exception as e:
                    pass

        pat_columns = re.compile("(.*-columns)")
        data_columns = soup.find('g', class_=pat_columns)

        if data_columns is not None:
            for item in data_columns:
                try:
                    y = item.attrs['height']
                    print(y)
                    dataValue.append(float(y)/float(height))
                except Exception as e:
                    pass
            return dataValue


def check_fusion_axes(soup):
    pat = re.compile("(.*-dataset-axis-name)")
    axes = soup.find_all('g', class_=pat)
    if axes is not None:  # there are axes labels
        axes_labels = []
        for i in range(len(axes)):
            try:
                axes_labels.append(axes[i].find('text').get_text())
            except Exception as e:
                pass

        if len(axes_labels) >= 2 and axes_labels.count('') == 0:  # we need at least 2 axes labelled
            return axes_labels  # [bottom, left, right]

    return False


def check_fusion_title(soup):
    title = soup.find('svg').find('title')

    if title is None or title == '':
        pat = re.compile("(.*-caption)")
        title = soup.find_all('g', class_=pat)
        if title is not None:
            try:
                title = title[0].find_all('text')
                title_text = []
                for i in range(len(title)):
                    title_text.append(title[i].get_text())
            except Exception as e:
                return False

            return ', '.join(title_text)  # return a string for consistency
    else:
        return title.get_text()

    return False


def check_fusion_legend(soup):
    pat = re.compile("(.*-legend)")
    legend = soup.find('g', class_=pat)

    if legend is not None:
        text = legend.find_all('text')
        legend_labels = []
        for i in text:
            legend_labels.append(i.get_text())
        return legend_labels

    return False


def read_svg_chart(soup, graph_type):
    if graph_type == SupportedType.LINE:
        graph_type = 'line'
        data_points = get_data_line_chart(soup)
    elif graph_type == SupportedType.SCATTER:
        graph_type = 'scatterplot'
        data_points = get_data_scatter_chart(soup)
    elif graph_type == SupportedType.BAR:
        graph_type = 'bar'
        data_points = get_data_bar_chart(soup)

    x_axis_values = check_fusion_x_axis_values(soup)
    y_axis_values = check_fusion_y_axis_values(soup)
    axes_labels = check_fusion_axes(soup)
    title_text = check_fusion_title(soup)

    if axes_labels and title_text and x_axis_values and y_axis_values:
        info = {
            "title": title_text,
            "x_axis_title": axes_labels[0],
            "y_axis_title": axes_labels[1],
            "x_tick_labels": x_axis_values,
            "y_tick_labels": y_axis_values,
            "data": data_points
        }
        return info  # valid chart
    return False  # invalid chart
