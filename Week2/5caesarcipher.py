#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    split_string = []
    for item in s:
        split_string.append(item)

    ascii_string = [ord(x) for x in split_string]               # if 65 > ord(x) < 122
    for i in range(len(ascii_string)):
        if ascii_string[i] >= 65 and ascii_string[i] <= 90:     # if upper case
            ascii_string[i] += k
            if ascii_string[i] > 90:
                ascii_string[i] = 64 + (ascii_string[i] - 90) % 26
        elif ascii_string[i] >= 97 and ascii_string[i] <= 122:  # if lower case
            ascii_string[i] += k
            if ascii_string[i] > 122:
                ascii_string[i] = 96 + (ascii_string[i] - 122) % 26

    string_converted = [chr(x) for x in ascii_string]
    joined_string = "".join(string_converted)

    return joined_string



if __name__ == '__main__':
    string = "What's up?"
    k = 1
    result = caesarCipher(string, k)
    print(result)