
def my_combinations(iterable, size):
    """
    The generator receives an iterable object, and a desired size,
     and produces a series of all possible combinations of the input size.
    >>> [i for i in my_combinations([1,2,3],2)]
    [[1, 2], [1, 3], [2, 3]]
    >>> [i for i in my_combinations(range(4),3)]
    [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]]
    >>> [i for i in my_combinations(range(0,20),50)]
    []
    >>> [i for i in my_combinations(range(0,20),20)]
    [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]]
    """
    pool = tuple(iterable)
    n = len(pool)
    if size > n:
        return
    indices = list(range(size))
    yield [pool[i] for i in indices]

    while True:
        for i in reversed(range(size)):
            if indices[i] != i + n - size:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, size):
            indices[j] = indices[j-1] + 1
        yield [pool[i] for i in indices]

def bounded_subsets_a(seq, c):
    """
    The generator receives as input a list S of different positive numbers,
    and some positive number C, and produces a series of all subsets of S, whose sum is at most C.
    >>> [i for i in bounded_subsets_a([1,2,3], 4)]# prints:
    [[], [1], [2], [3], [1, 2], [1, 3]]
    >>> [s for s in bounded_subsets_a(range(50,60), 103)]
    [[], [50], [51], [52], [53], [54], [55], [56], [57], [58], [59], [50, 51], [50, 52], [50, 53]]
    >>> [s for s in zip(range(5), bounded_subsets_a(range(100), 1000000000000))]
    [(0, []), (1, [0]), (2, [1]), (3, [2]), (4, [3])]
    """

    for pos, item in enumerate(seq):
        for comb in my_combinations(seq, pos):
            if sum(list(comb)) <= c:
                yield list(comb)
            else:
                break

def bounded_subsets(seq, c):
    """
    subsets_bounded. The generator receives as input a list S of different positive numbers,
    and some positive number C, and produces a series of all subsets of S, whose sum is at most C,
    in ascending order of their sum
    >>> [i for i in bounded_subsets([1,2,3], 4)]
    [[], [1], [2], [3], [1, 2], [1, 3]]
    >>> [s for s in bounded_subsets(range(50,60), 103)]
    [[], [50], [51], [52], [53], [54], [55], [56], [57], [58], [59], [50, 51], [50, 52], [50, 53]]
    >>> [s for s in zip(range(5), bounded_subsets(range(100), 1000000000000))]
    [(0, []), (1, [0]), (2, [1]), (3, [0, 1]), (4, [2])]
    """

    for curr in range(0, c+1):
        for pos, item in enumerate(seq):
            for comb in my_combinations(seq, pos):
                if sum(list(comb)) == curr:
                    yield list(comb)
                elif sum(list(comb)) > curr:
                    break

if __name__ == '__main__':

    import doctest
    doctest.testmod()

# I helped with the code: https://sparrow.dev/python-combinations/
