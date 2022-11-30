"""
URL:
https://www.codingame.com/ide/puzzle/genome-sequencing

My Solution:

import sys
import math
import itertools

# read the num of subsequences
n = int(input())
# read all the input subsequences
input_list = [input() for x in range(n)]

# get a list with all the possible permutations
permutations = list(itertools.permutations(input_list))

# The maximum possible size:
min_length = n * 10

# Checks for each permutation the minimum size:
for tup in permutations:

    first_str = tup[0]

    for next_str in itertools.islice(tup, 1, None):

        i = 0
        while i < len(first_str):
            # check if the next_str is contained in the first_str
            if next_str in first_str:
                break
            # check if the beginning of the next_str matches the end of the first_str
            index = len(first_str) - i
            if first_str[-index:] == next_str[:index]:
                first_str += next_str[index:]
                break
            i += 1

        if i == len(first_str):
            first_str += next_str

    min_length = min(min_length, len(first_str))

print(min_length)

# I helped with the code: https://github.com/charlesfranciscodev/codingame/blob/master/puzzles/python3/genome_sequencing.py

"""