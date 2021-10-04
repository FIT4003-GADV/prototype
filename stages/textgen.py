"""
Consists of the "TextGen" stage to generate alt-text for the input SVG vis.
"""
from typing import List

from absl import logging

from stages.stage import Stage
from stages.trend import TrendType
from supported_chart_types import SupportedType


class TextGen(Stage):
    def __init__(self, info: dict, chart_type: SupportedType, trend: dict):
        super().__init__()
        if not info:
            raise ValueError('No data provided to TextGen stage.')
        if not chart_type:
            raise ValueError('Chart type not provided to TextGen stage.')
        if not trend:
            raise ValueError('No trend provided to TextGen stage.')
        self.info = info
        self.chart_type = chart_type
        self.trend = trend

    def do_stage(self, *args, **kwargs) -> List[str]:
        """Returns an alt-text description of the SVG vis."""
        logging.info('Text generating...')
        result = ""
        if self.chart_type == SupportedType.BAR:
            if isinstance(self.trend['min'][1], (int, float)):
                max_value = round(self.trend['max'][1], 2)
                min_value = round(self.trend['min'][1], 2)
            else:
                max_value = self.trend['max'][1]
                min_value = self.trend['min'][1]

            result += f"A {self.chart_type.value} graph representing {self.info['title']} where {self.info['x_axis_title']} is plotted against {self.info['y_axis_title']}."
            result += f"This chart features the categories: {', '.join(self.info['x_tick_labels'])}."
            result += f"The highest category is {self.trend['max'][0]} with {max_value} {self.info['y_axis_title']}"
            result += f"The lowest category is {self.trend['min'][0]} with {min_value} {self.info['y_axis_title']}"
        else:
            result += f"A {self.chart_type.value} representing {self.info['title']} where {self.info['x_axis_title']}"
            result += f" is plotted against {self.info['y_axis_title']}.",
            result += f"This {self.chart_type.value} shows an {self.trend} trend."
        return result
