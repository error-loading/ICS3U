# 2D List - data organized in 2-dimensions

# e.g. chess
from pprint import *
board = [[0 for i in range(8)] for j in range(8)]
board[4][2] = 1
# pprint(board)

def flatten(arr):
    return [k for i in arr for k in i]

x = flatten(board)


def fold(lst, sz):
    return [lst[i:i+sz] for i in range(0, len(lst), sz)]


newArr = list(range(10, 30))
pprint(fold(newArr, ))
