"""
Consists of the "TextGen" stage to generate alt-text for the input SVG vis.
"""
from typing import List

from absl import logging
from bs4 import BeautifulSoup

from stages.stage import Stage
from stages.trend import TrendType
from supported_chart_types import SupportedType


class TextGen(Stage):
    def __init__(self, svg: BeautifulSoup, chart_type: SupportedType, trend: TrendType):
        super().__init__()
        if not svg:
            raise ValueError('No SVG provided to TextGen stage.')
        if not chart_type:
            raise ValueError('Chart type not provided to TextGen stage.')
        if not trend:
            raise ValueError('No trend provided to TextGen stage.')
        self.svg = svg
        self.chart_type = chart_type
        self.trend = trend

    def do_stage(self, *args, **kwargs) -> List[str]:
        """Returns an alt-text description of the SVG vis."""
        logging.info('Text generating...')
        # TODO
        return [f"A {self.chart_type} representing...", "This chart features..."]
