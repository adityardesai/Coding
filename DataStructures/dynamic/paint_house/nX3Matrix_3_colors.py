"""
You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colours: 
Red, Yellow or Green while making sure that no two adjacent cells have the same colour (i.e no two cells that share vertical or horizontal sides have the same colour).

You are given n the number of rows of the grid.

Return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 10^9 + 7.

 
Key Note:

There are only two possibilities to form a non-adjacent row: 3 colors combination (use all three colors, e.g., RYG) and 2 color combination 
(use only two of three colors, e.g., RYR).
We add the new row one by one. Apart from its inner adjacent relation, every new added row only relies on the previous one row 
(new added row is only adjacent with the row above it).
Every color combination follows the same pattern indicated below. 3-color combination can generate two 3-color combination, 
and two 2-color combination for the next round. 2-color combination can generate two 3-color combination, and three 2-color combination for the next round.
image

Let's try to have a math eqution to show the change above.
The number of 3-color combination for round n is: S(n). The number of 2-color combination for round n is T(n).
Thus, we can have two simple math equations reflecting the relation between current round (n) with next round (n + 1) for both 3-color-combination and 2-color-combination.

S(n + 1) = 2 * S(n) + 2 * T(n)
T(n + 1) = 2 * S(n) + 3 * T(n)

init: for the single row, there are C(3, 3) * 3! = 6 3-color combinations, and C(3, 2) * 2 = 6 2-color combinations.
C(3, 3) * 3! means: choose 3 colors out of 3, and, first cell: 3 possibilities, second cell: 2 possibilities, third cell: only 1 possibility.
C(3, 2) * 2 means: choose 2 colors out of 3, and, there are only two ways: ABA or BAB.


Ref:https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/discuss/574943/Java-Detailed-Explanation-with-Graph-Demo-DP-Easy-Understand
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
            
        
        
        
