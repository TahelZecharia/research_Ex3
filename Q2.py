from typing import List
from typing import Dict
from tsp import *
from typing import Callable, Any
import outputtypes as out

"""
Two simple algorithms for the traveling agent problem:
A simple algorithm: follows the order of the cities whose sum of all distances from the other cities is the smallest.
Greedy algorithm: starts from the first city and goes each time to the city closest to the current city
"""
a = [[-1, 10, 15, 20], [10, -1, 35, 25], [35, 15, -1, 30], [20, 25, 30, -1]]

b = {"0": {"0": -1, "1": 10, "2": 15, "3": 20},
    "1": {"0": 10, "1": -1, "2": 35, "3": 25},
    "2": {"0": 35, "1": 15, "2": -1, "3": 30},
    "3": {"0": 20, "1": 25, "2": 30, "3": -1}}

c = {"a": {"a": -1, "b": 9, "c": 4, "d": 2},
    "b": {"a": 9, "b": -1, "c": 77, "d": 2},
    "c": {"a": 88, "b": 66, "c": -1, "d": 8},
    "d": {"a": 8, "b": 7, "c": 8, "d": -1}}

def partition(algorithm: Callable, tsp: list, outputtype):

    """
    >>> partition(greedy, a, out.Length)
    'TSP length: 95'
    >>> partition(greedy, b, out.Length)
    'TSP length: 95'
    >>> partition(greedy, a, out.Path)
    'TSP path: [0, 1, 2, 3]'
    >>> partition(greedy, b, out.Path)
    "TSP path: ['0', '1', '2', '3']"
    >>> partition(simple, a, out.Length)
    'TSP length: 100'
    >>> partition(simple, b, out.Length)
    'TSP length: 100'
    >>> partition(simple, a, out.Path)
    'TSP path: [0, 1, 3, 2]'
    >>> partition(simple, b, out.Path)
    "TSP path: ['0', '1', '3', '2']"
    >>> partition(greedy, c, out.Path)
    "TSP path: ['a', 'd', 'b', 'c']"

    """

    if isinstance(tsp, dict):  # items is a dict mapping an item to its value.
        cities_names = list(tsp.keys())
        city_distances = lambda item_name: list(tsp[item_name].values())
    else:  # items is a list
        cities_names = [index for index in range(len(tsp))]
        city_distances = lambda item: tsp[item]

    my_tsp = outputtype.create_binner(city_distances)
    algo_tsp = algorithm(my_tsp, tsp, cities_names)
    return outputtype.extract_output(algo_tsp)


def simple(my_tsp: TSP, tsp: List[List[int]], cities_names):

    ans = my_tsp.new_tsp()
    for city in sorted(cities_names, key=lambda i: sum(my_tsp.valueof(i))):
        my_tsp.add_city(ans, city)
    return my_tsp.result(ans, tsp)


def greedy(my_tsp: TSP, tsp: List[List[int]], cities_names: list):

    tsp_copy: list = cities_names.copy()
    last_name = tsp_copy.pop(0)
    ans = my_tsp.new_tsp()
    my_tsp.add_city(ans, last_name)

    while len(tsp_copy) > 0:
        city = min(tsp_copy, key=lambda i: my_tsp.valueof(i)[cities_names.index(last_name)])
        tsp_copy.remove(city)
        my_tsp.add_city(ans, city)
        last_name = city

    return my_tsp.result(ans, tsp)


if __name__ == '__main__':

    import doctest
    doctest.testmod()
