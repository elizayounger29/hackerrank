#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    count = 0
    # how many sets of m fits into s: len(s) -
    number_of_slices = max(0, len(s) - m + 1)
    for i in range(number_of_slices):
        if sum(s[i:i + m]) == d:
            count += 1
    return count


if __name__ == '__main__':
    s = [2, 2, 1, 3, 2] # the segment list of integers s[n] = [2, 2, 1, 3, 2]
    d = 4 # the day ron was born. the sequence segment needs to add up to this number
    m = 2 # the month ron was born. the length of the segment needed.
    result = birthday(s, d, m)
    print(result)