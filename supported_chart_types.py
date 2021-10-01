"""
Consists of all supported chart types in the prototype.
"""
from enum import Enum


class SupportedType(Enum):
    # All line charts.
    LINE = 1
    # All bar charts.
    BAR = 2
    # Pie charts.
    PIE = 3
