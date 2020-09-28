"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

TC:O(N)
SC:O(N)

https://leetcode.com/problems/merge-intervals/
"""
from heapq import *
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])
        min_heap = list()
        
        min_heap.append(intervals[0])
        
        for i in range(1, len(intervals)):
            next_interval=intervals[i]
            if min_heap[-1][1]>=next_interval[0]:
                min_heap[-1][1]=max(next_interval[1],min_heap[-1][1])
            else:
                heappush(min_heap, next_interval)
        
        return min_heap
        
        
        
