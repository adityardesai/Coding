# https://www.hackerrank.com/challenges/two-strings/problem

import math
import os
import random
import re
import sys


# Complete the twoStrings function below.
def twoStrings(s1, s2):

    if not s1 or not s2:
        return -1

    h_set1 = set()
    h_set2 = set()

    for ch in s1:
        h_set1.add(ch)

    for ch in s2:
        h_set2.add(ch)

    if h_set1.intersection(h_set2):
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
