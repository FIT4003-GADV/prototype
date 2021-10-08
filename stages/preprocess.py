"""
Consists of the "Preprocess"ing stage to run any pre-processing needed on an input SVG vis.
"""
from absl import logging
from bs4 import BeautifulSoup
import re

from stages.stage import Stage
from supported_chart_types import SupportedType
from stages.logic.preprocess.plotly import read_plotly_chart
from stages.logic.preprocess.fusion import read_fusion_chart


class Preprocess(Stage):
    def __init__(self, svg_string: str, chart_type: SupportedType):
        super().__init__()
        if not svg_string:
            raise ValueError('No SVG provided to Preprocess stage.')
        if not chart_type:
            raise ValueError('No chart type specified to Preprocess stage.')
        self.svg_string = svg_string
        self.chart_type = chart_type

    def do_stage(self, *args, **kwargs) -> dict:
        """Pre-processes an input SVG vis and returns it once pre-processed."""
        logging.info('Preprocessing...')
        soup = BeautifulSoup(self.svg_string, 'html.parser')
        return self.check_graph_source(soup)

    def check_graph_source(self, soup):
        """
        Checks the source of the chart. 
        Supported types: plotly, fusion
        """
        fusion_pat = re.compile("(.*-dataset-axis-name)")
        axes = soup.find_all('g', class_=fusion_pat)
        if len(axes) == 0:
            axes = soup.find_all('g', class_='g-xtitle')
            if len(axes) > 0:
                logging.info('This is a plotly chart.')
                return read_plotly_chart(soup, self.chart_type)
        elif len(axes) > 0:
            logging.info('This is a fusion chart.')
            return read_fusion_chart(soup, self.chart_type)
        raise Exception("Chart source not supported")

