#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):

    for row in range(len(grid)):            # order the rows
        temp = []
        for letter in grid[row]:
            temp.append(ord(letter))
        temp = sorted(temp)
        temp_chr = [chr(x) for x in temp]
        grid[row] = ''.join(temp_chr)

    columns = len(grid)
    for column in range(columns):
        temp = []
        for row in range(columns):
            temp.append(ord(grid[column+row]))
        print(temp)

    return grid
    # Rearrange each row to be ascending
    # then check whether each column is in ascending value
    # if everything checkso out, return YES
    # else, return NO


if __name__ == '__main__':
    grid = ['abc', 'def', 'ghi']
    result = gridChallenge(grid)
    print(result)