# https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid/problem
# TC: O(N*M)
# SC: O(1)

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maxRegion function below.
def is_valid(grid, x, y):
    if x < 0 or y < 0 or x > len(grid) - 1 or y > len(grid[0]) - 1:
        return False
    return True


def dfs(grid, r, c):

    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1),
                  (-1, -1)]
    grid[r][c] = -1
    count = 1
    for d in DIRECTIONS:
        n_r = d[0] + r
        n_c = d[1] + c
        if is_valid(grid, n_r, n_c) and grid[n_r][n_c] == 1:
            count += dfs(grid, n_r, n_c)
    return count


def maxRegion(grid):
    if not grid:
        return grid

    r = len(grid)
    c = len(grid[0])
    gcount = 0

    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1:
                gcount = max(gcount, dfs(grid, i, j))
    return gcount


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()
