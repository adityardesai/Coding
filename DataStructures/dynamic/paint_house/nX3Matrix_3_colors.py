
# 
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
            
        
        
        
