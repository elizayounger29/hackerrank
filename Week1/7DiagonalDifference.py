#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    n = len(arr)
    l_diagonal = [arr[i][i] for i in range(n)]
    r_diagonal = [arr[i][(n - 1) - i] for i in range(n)]
    if sum(l_diagonal) > sum(r_diagonal):
        difference = sum(l_diagonal) - sum(r_diagonal)
    else:
        difference = sum(r_diagonal) - sum(l_diagonal)
    return difference

if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, -12]
    ]

    result = diagonalDifference(matrix)

    print(result)
