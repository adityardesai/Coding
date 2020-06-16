# https://www.hackerrank.com/challenges/minimum-swaps-2/problem 

import math
import os
import random
import re
import sys


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    if not arr:
        return -1

    i = 0
    count = 0
    while i < len(arr):
        j = arr[i] - 1
        if arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            count += 1
        else:
            i = i + 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
