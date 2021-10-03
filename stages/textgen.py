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
        logging.info(self.info)
        logging.info(self.chart_type)
        logging.info(self.trend)
        if self.chart_type == SupportedType.BAR:
            return [
                f"A {self.chart_type.value} graph representing {self.info['title']} where {self.info['x_axis_title']}"
                f" is plotted against {self.info['y_axis_title']}.",
                f"This chart features the categories: {', '.join(self.info['x_tick_labels'])}.",
                f"The highest category is {self.trend['max'][0]} with {round(self.trend['max'][1], 1)} {self.info['y_axis_title']}",
                f"The lowest category is {self.trend['min'][0]} with {round(self.trend['min'][1], 1)} {self.info['y_axis_title']}"]
        else:
            return [f"A {self.chart_type.value} representing {self.info['title']} where {self.info['x_axis_title']}"
                    f" is plotted against {self.info['y_axis_title']}.",
                    f"This {self.chart_type.value} shows an {self.trend} trend."]
