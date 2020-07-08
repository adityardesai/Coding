# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
# TC:O(NlogN)
# SC:O(1)
from heapq import *


class Solution:
    def non_heap_helper(self, points):
        points.sort(key=lambda x: x[1])
        common = 1
        first_end = points[0][1]

        for x_start, x_end in points:
            if first_end < x_start:
                common += 1
                first_end = x_end

        return common

    def findMinArrowShots(self, points: List[List[int]]) -> int:

        if not points:
            return 0
        return self.non_heap_helper(points)
