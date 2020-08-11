# https://leetcode.com/problems/best-time-to-buy-and-sell-stock
# TC: O(N)
# SC: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_price=prices[0]
        max_profit=0
        
        for i in range(1, len(prices)):
            if prices[i]<min_price:
                min_price=prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit=prices[i] - min_price
        
        return max_profit
                
        