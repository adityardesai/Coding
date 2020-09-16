"""

There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

https://leetcode.com/problems/paint-house-ii

TC:O(NK)
SC:O(1)
"""


class Solution:
    
    def minCostII(self, costs: List[List[int]]) -> int:
        
        n=len(costs)
        if n==0: return 0
        k=len(costs[0])
        
        for house in range(1,n):
            min_color=None
            second_min_color=None
            
            for color in range(k):
                cost = costs[house-1][color]
                
                if min_color is None or cost<costs[house-1][min_color]:
                    second_min_color = min_color
                    min_color=color
                elif second_min_color is None or cost<costs[house-1][second_min_color]:
                    second_min_color=color
        
            for color in range(k):
                if color==min_color:
                    costs[house][color] += costs[house-1][second_min_color]
                else:
                    costs[house][color] += costs[house-1][min_color]
        return min(costs[-1])
                    
        
        
