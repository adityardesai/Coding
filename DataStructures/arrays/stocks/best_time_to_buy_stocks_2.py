# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# TC:O(N)
# SC:O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0
        
        max_profit=0
        for i in range(1,len(prices)):
            if(prices[i]>prices[i-1]):
                max_profit+=prices[i] - prices[i-1]
        return max_profit