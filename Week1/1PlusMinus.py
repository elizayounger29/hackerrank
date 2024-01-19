#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    array = arr
    plus = 0
    zero = 0
    minus = 0
    length = len(array)

    for number in array:

        if number > 0:
            plus += 1
        if number == 0:
            zero += 1
        if number < 0:
            minus += 1

    plus = float(format(plus / length, '.6f'))
    zero = float(format(zero / length, '.6f'))
    minus = float(format(minus / length, '.6f'))

    print("{:.6f}".format(plus))
    print("{:.6f}".format(minus))
    print("{:.6f}".format(zero))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

