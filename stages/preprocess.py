"""
Consists of the "Preprocess"ing stage to run any pre-processing needed on an input SVG vis.
"""
from absl import logging
from bs4 import BeautifulSoup

from stages.stage import Stage


class Preprocess(Stage):
    def __init__(self, svg_string: str):
        super().__init__()
        if not svg_string:
            raise ValueError('No SVG provided to Preprocess stage.')
        self.svg_string = svg_string

    def do_stage(self, *args, **kwargs) -> BeautifulSoup:
        """Pre-processes an input SVG vis and returns it once pre-processed."""
        logging.info('Preprocessing...')
        return BeautifulSoup(self.svg_string, 'html.parser')
