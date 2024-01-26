#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#



# A = [1, 1, 2, 2]
# B = [4, 3, 3, 3]


def twoArrays(k, A, B):
    a_sorted = sorted(A, reverse=True)
    b_sorted = sorted(B)

    for item in range(len(a_sorted)):
        if not a_sorted[item] + b_sorted[item] >= k:
            return "NO"
    return "YES"


if __name__ == '__main__':
    A = [1, 2, 2, 1]
    B = [3, 3, 3, 4]
    k = 4
    result = twoArrays(k, A, B)
    print(result)
