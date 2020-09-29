"""
Implement int sqrt(int x).
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

TC:O(logN)
SC:O(1)
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x<2:
            return x
        
        start=2
        end=x//2
        
        while start<=end:
            mid = (start+end) //2
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                start=mid+1
            else:
                end=mid-1
        
        return end
