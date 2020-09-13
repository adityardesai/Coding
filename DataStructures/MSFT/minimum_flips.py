# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/
# TC:O(N)
# SC:O(1)

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        
        result=0
        
        while a!=0 or b!=0 or c!=0:
            r1=a%2
            r2=b%2
            r3=c%2
            
            if r3==0:
                result+=(r1+r2)
            else:
                if r1+r2==0:
                    result+=1
            
            a=a//2
            b=b//2
            c=c//2
        
        return result
        

