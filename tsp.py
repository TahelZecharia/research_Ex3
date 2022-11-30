"""

"""

from abc import ABC, abstractmethod
from typing import Any, Callable, List, Tuple, Iterator

class TSP(ABC):
    """
    An abstract bins-array manager.

    All arrays created by the same binner share the following two variables:
     * numbins - the total number of bins.
     * valueof - a function that maps an item to its value.
    """

    def __init__(self, valueof: Callable = lambda x: x):
        self.valueof = valueof

    @abstractmethod
    def new_tsp(self) -> Any:
        '''
        Create a new bins-array with numbins bins.
        '''
        return None

    @abstractmethod
    def add_city(self, path: list, city: Any) -> Any:
        """
        Add the given item to the given bin in the given array.
        Return the bins after the addition.
        """
        return path

    @abstractmethod
    def result(self, path: list, tsp) -> Any:
        """
        Return only the current sums.
        """
        return None


class TSPpath(TSP):

    def __init__(self, valueof: Callable = lambda x: x):
        super().__init__(valueof)

    # Here, the bins-array is simply an array of the sums.

    def new_tsp(self) -> List:
        return []

    def add_city(self, path: list, city: Any) -> list:
        path.append(city)
        return path

    def result(self, path: list, tsp) -> list:
        return path


class TSPlength(TSP):

    def __init__(self, valueof: Callable = lambda x: x):
        super().__init__(valueof)

    def new_tsp(self) -> list:
        return []

    def add_city(self, path: list, city: Any) -> list:
        path.append(city)
        return path

    def result(self, path: list, tsp) -> int:
        ans = 0
        for index in range(0, len(path)-1):
            ans += tsp[path[index]][path[index+1]]
        ans+=tsp[path[len(path)-1]][path[0]]
        return ans



