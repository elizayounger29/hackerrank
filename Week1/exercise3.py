#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hour = s[:2]
    filling = s[2:8]
    am_pm = s[-2:]

    if am_pm == "PM":
        # 12 are edge cases
        if hour != "12":
            temp = int(hour)
            temp = temp + 12
            hour = str(temp)

    if am_pm == "AM":
        if hour == "12":
            hour = "00"

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = "12:01:00AM"

    result = timeConversion(s)

    print(result)
