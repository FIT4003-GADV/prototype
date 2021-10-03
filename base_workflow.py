"""
The Stage orchestrator.
"""
from typing import List

# from stages import Predict
from stages import Preprocess
from stages import TextGen
from stages import Trend
from stages import TrendType
from supported_chart_types import SupportedType


class BaseWorkflow(object):
    def __init__(self, svg_string: str):
        self.svg_string = svg_string

    def execute(self) -> List[str]:
        # chart_type: SupportedType = Predict(svg).do_stage()
        chart_type: SupportedType = SupportedType.SCATTER
        info: dict = Preprocess(self.svg_string, chart_type).do_stage()
        trend_type: dict = Trend(info, chart_type).do_stage()

        alt_text: List[str] = TextGen(info, chart_type, trend_type).do_stage()

        return alt_text
