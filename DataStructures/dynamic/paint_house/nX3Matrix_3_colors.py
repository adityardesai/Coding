"""
You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colours: Red, Yellow or Green while making sure that no two adjacent cells have the same colour (i.e no two cells that share vertical or horizontal sides have the same colour).

You are given n the number of rows of the grid.

Return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 10^9 + 7.

 

"""
# https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/
# TC: 
# SC: 
class Solution:
    def numOfWays(self, n: int) -> int:
        """
        S(n + 1) = 2 * S(n) + 2 * T(n)
        T(n + 1) = 2 * S(n) + 3 * T(n)
        """
        MOD = 10**9 + 7
        if not n:
            return
        
        color3=6 # abc, acb, bca, bac, cab, cba
        color2=6 # aba, bab, bcb, cbc, aca, cac
        
        for i in range(2, n+1):
            tempcolor=color3
            color3=(2 * color3 + 2 * color2) % MOD 
            color2=(2*tempcolor + 3 * color2) % MOD
        
        return (color3+color2) % MOD
            
        
        
        
