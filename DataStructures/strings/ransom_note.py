# https://www.hackerrank.com/challenges/ctci-ransom-note/problem

import math
import os
import random
import re
import sys


# Complete the checkMagazine function below.
def checkMagazine(magazine, note):

    if not magazine or not note:
        print('No')
    h_map = dict()

    for word in magazine:
        h_map[word] = h_map.get(word, 0) + 1

    for word in note:
        if word in h_map and h_map.get(word) > 0:
            h_map[word] = h_map[word] - 1
        else:
            print('No')
            return

    print('Yes')


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
