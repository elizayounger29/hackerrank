#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    s = s.lower()
    alphabet = {chr(char): 0 for char in range(97, 123)}
    for letter in s:
        if letter in alphabet:
            alphabet[letter] += 1

    for letter in alphabet:
        if alphabet[letter] == 0:
            return "not pangram"

    return "pangram"

if __name__ == '__main__':
    string = "We promptly judged antique ivory buckles for the next prize"
    result = pangrams(string)
    print(result)