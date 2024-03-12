#!/bin/python3

import math
import os
import random
import re
import sys

# def towerBreakers(n, m):
#
#     tower_num = n
#     tower_height = []
#     for tower in range(tower_num):      # [6, 6]
#         tower_height.append(m)
#
#     player_turn = 0
#
#     for tower in tower_height:          # count how many times you can half the height
#         while tower % 2 == 0:
#             tower = tower / 2
#             player_turn += 1
#
#     for tower in tower_height:          # count how moves are available after the halving
#         if tower > 1:
#             tower == 1
#             player_turn += 1
#
#     if player_turn % 2 == 0:            # if player_turn is even, player 2 winner
#         return 2
#     else:
#         return 1                        # vice versa
#
#
# if __name__ == '__main__':
#     n = 3   # number of towers
#     m = 6   # height of towers
#     result = towerBreakers(n, m)
#     print(result)
#
# # 6, 6, 6
# # 6 moves
# # start player 1 + 4 moves = 2 winner
# #

def towerBreakers(n, m):
    if m == 1 or n % 2 == 0:
        return 2
    else:
        return 1


if __name__ == '__main__':
    n = 3   # number of towers
    m = 6   # height of towers
    result = towerBreakers(n, m)
    print(result)

# 6, 6, 6
# 6 moves
# start player 1 + 4 moves = 2 winner
#