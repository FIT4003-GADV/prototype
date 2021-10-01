"""
Consists of the "Trend" stage to find trends in an input SVG.
"""
from enum import Enum

from absl import logging
from bs4 import BeautifulSoup

from stages.stage import Stage
from supported_chart_types import SupportedType


class TrendType(Enum):
    INCREASING = 1
    DECREASING = 2
    FLAT = 3


class Trend(Stage):
    def __init__(self, svg: BeautifulSoup, chart_type: SupportedType):
        super().__init__()
        if not svg:
            raise ValueError('No SVG provided to Trend stage.')
        if not chart_type:
            raise ValueError('Chart type not provided to Trend stage.')
        self.svg = svg
        self.chart_type = chart_type

    def do_stage(self, *args, **kwargs) -> TrendType:
        """Runs stat models to identify trends in the input SVG vis."""
        logging.info('Trend finding...')
        # Return a hardcoded value for now.
        return TrendType.INCREASING
