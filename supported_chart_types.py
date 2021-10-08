"""
Consists of all supported chart types in the prototype.
"""
from enum import Enum


class SupportedType(Enum):
    # All line charts.
    LINE = "line"
    # All bar charts.
    BAR = "bar"
    # Scatterplot charts.
    SCATTER = "scatterplot"
