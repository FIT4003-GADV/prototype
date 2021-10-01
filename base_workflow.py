"""
The Stage orchestrator.
"""
from typing import List

from bs4 import BeautifulSoup

from stages import Predict
from stages import Preprocess
from stages import TextGen
from stages import Trend
from stages import TrendType
from supported_chart_types import SupportedType


class BaseWorkflow(object):
    def __init__(self, svg_string: str):
        self.svg_string = svg_string

    def execute(self) -> List[str]:
        svg: BeautifulSoup = Preprocess(self.svg_string).do_stage()
        chart_type: SupportedType = Predict(svg).do_stage()
        trend_type: TrendType = Trend(svg, chart_type).do_stage()

        alt_text: List[str] = TextGen(svg, chart_type, trend_type).do_stage()

        return alt_text
