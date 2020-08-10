# https://leetcode.com/problems/two-city-scheduling/
# TC: O(NlogN)
# SC: O(1)
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        costs.sort(key=lambda x: x[0] - x[1])

        result = 0
        n = len(costs) // 2

        for i in range(n):
            result = result + costs[i][0]

        for i in range(n, len(costs)):
            result = result + costs[i][1]

        return result
