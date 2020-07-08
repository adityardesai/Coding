# https://leetcode.com/problems/merge-intervals/
# TC:O(NlogN)
# SC:O(N) . If sorting is done in place, then its O(1)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = list()
        if not intervals:
            return result

        intervals.sort(key=lambda x: x[0])

        result.append(intervals[0])

        for i in range(1, len(intervals)):
            next_interval = intervals[i]

            if result[-1][1] >= next_interval[0]:
                result[-1][1] = max(result[-1][1], next_interval[1])
            else:
                result.append(next_interval)
        return result
