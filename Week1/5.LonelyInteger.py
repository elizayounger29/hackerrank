#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    list_items = {}
    result = ''
    for item in a:
        if item in list_items:
            list_items[item] += 1
        else:
            list_items[item] = 1

    for key, value in list_items.items():
        if value < 2:
            result = key

    return result

    # Write your code here


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # n = int(input().strip())
    #
    # a = list(map(int, input().rstrip().split()))
    a = [1, 2, 3, 4, 3, 2, 1]
    result = lonelyinteger(a)
    print(result)
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
