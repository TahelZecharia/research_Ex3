"""
Define the various available output formats for a partition algorithm.
"""

from abc import ABC
from typing import Any, List, Callable
from tsp import *

BinsArray = Any

class OutputType(ABC):

    @classmethod
    def create_binner(cls, valueof: Callable) -> Any:
        """
        Construct and return a Bins structure. Used at the initialization phase of an algorithm.
        """
        raise NotImplementedError("Choose a specific output type")

    @classmethod
    def extract_output(cls, output: Any) -> Any:
        """
        Return the required output from the given bins-array.
        """
        raise NotImplementedError("Choose a specific output type")


class Path(OutputType):
    """ Output the list of sums of all bins (but not the bins' contents).  """
    @classmethod
    def create_binner(cls, valueof: Callable) -> Any:
        return TSPpath(valueof)

    @classmethod
    def extract_output(cls, path: list) -> str:
        return f"TSP path: {path}"


class Length(OutputType):
    """ Output the largest bin sum. """

    @classmethod
    def create_binner(cls, valueof: Callable) -> Any:
        return TSPlength(valueof)

    @classmethod
    def extract_output(cls, length: int) -> str:
        return f"TSP length: {length}"
