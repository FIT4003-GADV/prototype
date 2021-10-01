"""
Consists of the Abstract "Stage" class.
"""
from abc import ABC
from abc import abstractmethod
from typing import Any


class Stage(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def do_stage(self, *args, **kwargs) -> Any:
        """
        Executes the logic in this Stage.
        :param args: list of optional arguments passed into this Stage.
        :param kwargs: list of optional keyword arguments passed into this Stage.
        :return: the result of executing the logic in this Stage.
        """
        pass
