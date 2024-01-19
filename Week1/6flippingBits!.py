#!/bin/python3

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    return 2**32 + ~n
# n = 5
# n = 00000000000000000000000000000101
# ~n = 11111111111111111111111111111010
#  return 10000000000000000000000000000000 + -11111111111111111111111111111010

if __name__ == '__main__':
    # n = "1001" # 9 to 6
    length = 1
    n = "1001001"  # 9 to 6
    result = flippingBits(length)
    print(result)
    result = flippingBits(n)
    # result = flippingBits(n)
    print(result)
