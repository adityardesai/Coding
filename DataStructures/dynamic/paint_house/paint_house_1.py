"""
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.


https://leetcode.com/problems/paint-house/
TC: 
SC:
"""

class Solution:
    def __init__(self):
        self.costs = None
        self.memo = dict()
    def paint_brute_force(self, house, paint):
        total_cost = self.costs[house][paint]
        if house == len(self.costs)-1:
            pass
        elif paint==0:
            total_cost += min(self.paint_brute_force(house+1,1), self.paint_brute_force(house+1,2))
        elif paint==1:
            total_cost += min(self.paint_brute_force(house+1,0), self.paint_brute_force(house+1,2))
        elif paint==2:
            total_cost += min(self.paint_brute_force(house+1,0), self.paint_brute_force(house+1,1))
        
        return total_cost
    
    def paint_memoization(self, house, paint):
        if (house,paint) in self.memo:
            return self.memo[(house, paint)]
            
        total_cost = self.costs[house][paint]
        
        if house == len(self.costs)-1:
            pass
        elif paint==0:
            total_cost += min(self.paint_brute_force(house+1,1), self.paint_brute_force(house+1,2))
        elif paint==1:
            total_cost += min(self.paint_brute_force(house+1,0), self.paint_brute_force(house+1,2))
        elif paint==2:
            total_cost += min(self.paint_brute_force(house+1,0), self.paint_brute_force(house+1,1))
        
        self.memo[(house,paint)] = total_cost
        return total_cost
    
    def brute_force(self):
        a=self.paint_brute_force(0,0)
        b=self.paint_brute_force(0,1)
        c=self.paint_brute_force(0,2)
        return min(a,b,c)
    
    def memoization(self):
        a=self.paint_brute_force(0,0)
        b=self.paint_brute_force(0,1)
        c=self.paint_brute_force(0,2)
        return min(a,b,c)
    def dynamic_programming(self, costs):
        n=len(costs)
        if n==0: return 0
        k=3
              
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
    
    def minCost(self, costs: List[List[int]]) -> int:   
        if not costs:
            return 0
        self.costs=costs
        #return self.brute_force()
        #return self.memoization()
        return self.dynamic_programming(costs)
        
