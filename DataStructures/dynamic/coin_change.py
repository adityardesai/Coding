# https://leetcode.com/problems/coin-change/


class Solution:
    def helper_bottom_up(self, coins, amount):
        """
        TC: O(S*n)
        SC: O(S)
        Where S=amount and n=number of denominations
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[amount] != float('inf'):
            return dp[amount]
        else:
            return -1

    def helper_top_down(self, coins, remaining_amount, count):
        """
        TC:O(S*n)
        SC:O(S)
        Where S=amount and n=number of denominations
        """
        if remaining_amount < 0:
            return -1
        if remaining_amount == 0:
            return 0

        if count[remaining_amount - 1]:
            return count[remaining_amount - 1]

        min_coins = float('inf')

        for coin in coins:
            result = self.helper_top_down(coins, remaining_amount - coin,
                                          count)
            if result >= 0 and result < min_coins:
                min_coins = 1 + result

        if min_coins == float('inf'):
            min_coins = -1

        count[remaining_amount - 1] = min_coins
        return count[remaining_amount - 1]

    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount < 1:
            return 0

        return self.helper_top_down(coins, amount, [0] * amount)
