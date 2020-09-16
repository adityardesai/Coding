"""
We can use dynamic programming to solve this problem. Let's define dp(i, j, k) as follows:

i: we are dealing with the i-th house now
j: the previous hosue was painted with color j
k: houses[:i] formed k neighborhoods
And dp(i, j, k) means the total cost to paint houses[i:] under the current (j, k) constraint.

The transition function has two cases:

houses[i] is already painted
houses[i] needs to be painted
For the first case, the transition function is:

dp(i, j, k) = dp(i + 1, houses[i], k + (houses[i] != j))
Here houses[i] means the color of the current house. k + (houses[i] != j) means the number of neiborhoods after considering the i-th house.

For the second case, suppose we are painting houses[i] with color and its cost is paint_cost, then the transition function is:

dp(i, j, k) = paint_cost + dp(i + 1, color, k + (color != j))
We just need to iterate through the cost array and find out the optimal color for houses[i].

Time complexity: O(m * n * target * m)
Space complexity: O(m * n * target)
"""

from functools import lru_cache

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        
        @lru_cache(None)
        def dp(i, j, k):
            # base case 1. the painted houses already formed > target neighborhoods
            if k > target:
                return math.inf
            
            # base case 2. we have painted m houses
            if i == m:
                # base case 2.1. these m houses form target neighborhoods exactly
                if k == target:
                    return 0
                # base case 2.2. these m houses form < target neighborhoods
                else:
                    return math.inf
            
            # case 1. the i-th house is already painted
            if houses[i]:
                return dp(i + 1, houses[i], k + (houses[i] != j))
            
            # case 2. we need to pick a color for the i-th house
            ans = math.inf
            for color, paint_cost in enumerate(cost[i], 1):
                ans = min(ans, paint_cost + dp(i + 1, color, k + (color != j)))
            
            return ans
        
        tmp = dp(0, 0, 0)
        return tmp if tmp < math.inf else -1
