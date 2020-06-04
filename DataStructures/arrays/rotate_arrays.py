#!/bin/python3

# Hacker Rank Problem
# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem


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
