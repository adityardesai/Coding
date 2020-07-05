#https://leetcode.com/problems/power-of-three/
class Solution:
    def helper_loop(self, n):
        """
        Time complexity here is O(log(n) to the base 3)
        Can be language dependent
        Space complexity is O(1)
        """
        while n % 3 == 0:
            n = n / 3
        return n == 1

    def helper_log(self, n):
        """
        n=3^i
        i=log3(n)
        i=logb(n)/logb(3)
        
        Time complexity here depends on how log10 is implemented
        Space complexity is O(1)
        """
        numerator = log10(n)
        denominator = log10(3)

        return (numerator / denominator) % 1 == 0

    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        #return self.helper_loop(n)
        return self.helper_log(n)
