"""
Consists of the "Trend" stage to find trends in an input SVG.
"""
from enum import Enum

from absl import logging

from stages.stage import Stage
from supported_chart_types import SupportedType
from stages.logic.trend.bargraph_trend import trend_bar
from stages.logic.trend.linear_regression import trend_generator


class TrendType(Enum):
    INCREASING = 1
    DECREASING = 2
    FLAT = 3


class Trend(Stage):
    def __init__(self, info: dict, chart_type: SupportedType):
        super().__init__()
        if not info:
            raise ValueError('No data provided to Trend stage.')
        if not chart_type:
            raise ValueError('Chart type not provided to Trend stage.')
        self.info = info
        self.chart_type = chart_type

    def do_stage(self, *args, **kwargs) -> dict:
        """Runs stat models to identify trends in the input SVG vis."""
        logging.info('Trend finding...')
        if self.chart_type == SupportedType.BAR:
            # TODO: how to handle bar trend with enum?
            result = trend_bar(self.info)
            return {
                "max": result[0],
                "min": result[1]
            }
        else:
            return trend_generator(self.info)

