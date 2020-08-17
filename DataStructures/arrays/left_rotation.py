#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the rotLeft function below.
def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


def rotLeft(arr, d):
    if not arr:
        return
    reverse(arr, 0, d - 1)
    reverse(arr, d, len(arr) - 1)
    reverse(arr, 0, len(arr) - 1)
    return arr


def rotRight(arr, d):
    if not arr:
        return
    reverse(arr, 0, len(arr) - 1)
    reverse(arr, 0, d - 1)
    reverse(arr, d, len(arr) - 1)
    return arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int, input().rstrip().split()))
    result = rotLeft(a, d)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
