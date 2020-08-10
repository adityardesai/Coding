# https://leetcode.com/problems/k-closest-points-to-origin/
# TC:O(N)
# SC:O(N)
from heapq import *


class Solution:
    def min_heap_helper(self, points, K):
        min_heap = list()

        for i in range(len(points)):
            point = points[i]
            distance = sqrt(point[0] * point[0] + point[1] * point[1])
            min_heap.append((distance, i))

        heapify(min_heap)

        result = list()
        while K:
            pop = heappop(min_heap)
            result.append(points[pop[1]])
            K = K - 1

        return result

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if not points:
            return points
        return self.min_heap_helper(points, K)
