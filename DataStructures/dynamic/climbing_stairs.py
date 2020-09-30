"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

https://leetcode.com/problems/climbing-stairs/

TC:O(N)
SC:O(N)
"""

class Solution:
    def recursive(self, n, step):
        if step>n:
            return 0
        if step==n:
            return 1
        
        return self.recursive(n,step+1) + self.recursive(n,step+2) 
    
    def memoization(self, n, step, cache):
        if step>n:
            return 0
        
        if step==n:
            return 1
        
        if cache.get(step):
            return cache[step]
        
        cache[step] = self.memoization(n,step+1, cache) + self.memoization(n,step+2, cache)
        
        return cache[step]
    
    def dynamic_helper(self, n):
        if n==1:
            return 1
        
        dp=[0] * (n+1)
        dp[1]=1
        dp[2]=2
        
        for i in range(3, n+1):
            dp[i]=dp[i-1]+dp[i-2]
        
        return dp[n]
    
    def climbStairs(self, n: int) -> int:
        #return self.recursive(n, step=0)
        step=0
        cache=dict()
        #return self.memoization(n,step,cache)
        return self.dynamic_helper(n)
        
