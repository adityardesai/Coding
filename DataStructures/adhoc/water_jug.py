# https://leetcode.com/problems/water-and-jug-problem/
# TC:O(logN)N is max of (x,y)
# SC:O(1)
class Solution:
    def get_gcd(self, x, y):
        while y:
            temp = y
            y = x % y
            x = temp
        return x

    def helper_measure(self, x, y, z):

        if x + y < z:
            return False

        if x == z or x == y or x + y == z:
            return True

        gcd = self.get_gcd(x, y)
        return z % gcd == 0

    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        return self.helper_measure(x, y, z)
