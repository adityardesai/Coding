# https://leetcode.com/problems/unique-paths/
# TC:O(N*M)
# SC:O(N*M)
class Solution:
    def recursive_helper(self, m, n):
        if m == 1 or n == 1:
            return 1
        return self.recursive_helper(m - 1, n) + self.recursive_helper(
            m, n - 1)

    def dynamic_helper(self, m, n):
        dp = [[1] * n for x in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

    def uniquePaths(self, m: int, n: int) -> int:
        #return self.recursive_helper(m,n)
        return self.dynamic_helper(m, n)
