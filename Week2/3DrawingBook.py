#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    page_number = math.ceil((n + 1) / 2)        # How many pages in the whole book
    given_page = math.ceil((p + 1) / 2)         # What page are you looking for
    from_end = page_number - given_page     # How many page turns from end
    from_start = given_page - 1             # How many page turns from start

    if from_end >= from_start:               # Navigate from start
        return from_start
    elif from_end < from_start:             # Navigate from end
        return from_end


if __name__ == '__main__':
    n = 5
    p = 4
    result = pageCount(n, p)
    print(result)