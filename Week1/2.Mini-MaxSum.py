#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    array = sorted(arr)
    minimum = array[:-1]  # length - 2
    maximum = array[1:]
    print(f"{sum(minimum)} {sum(maximum)}")


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
