#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'maxMin' function below.

# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr


# def maxMin(k, arr):
#     sorted_arr = sorted(arr)
#     # print(f"sorted array =                             {sorted_arr}")   # arrange in order
#
#     distance = [sorted_arr[i+1] - sorted_arr[i] for i in range(len(sorted_arr)-1)]      # list of relationships
#     # print(f"relationships between the array elements =   {distance}")  # arrange in order
#
#     # print(f"k =                                        {sorted_arr[:len(arr) - k - 1]}")
#
#     distance_size = len(distance)
#     new_k = k - 1
#     possible_iterations = distance_size - (new_k - 1)
#     # print(f"possible iterations over the relationships array: {possible_iterations}")
#
#     temp = []
#
#     for x in range(possible_iterations):        # find out which grouping has overall smallest difference
#         temp.append(sum(distance[x:x+new_k]))
#
#     return min(temp)
#
#     # min_index = min(range(len(temp)), key=lambda i: temp[i])
#     # # print(f"index of winning combination: {min_index}")
#     # winner = sorted_arr[min_index: min_index + k]
#     # return winner

def maxMin(k, arr):
    sorted_arr = sorted(arr)
    print(f"sorted array: {sorted_arr}")

    min_diff = float('inf')  # Initialize min_diff with positive infinity

    iterations = len(arr) - (k-1)
    print(f"iterations: {iterations}")

    for i in range(iterations):
        current_diff = sorted_arr[i+(k-1)] - sorted_arr[i]
        if current_diff < min_diff:
            min_diff = current_diff

    return min_diff


if __name__ == '__main__':
    arr = [1, 10, 6, 11, 12]
    k = 3

    result = maxMin(k, arr)
    print(result)

# [1, 2, 6, 9, 12]
#  [1, 4,  3, 3]
#   [