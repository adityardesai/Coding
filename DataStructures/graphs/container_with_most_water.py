# https://leetcode.com/problems/container-with-most-water/
# TC:O(N)
# SC:O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:

        max_area = float('-inf')
        i = 0
        j = len(height) - 1

        while (i < j):
            max_area = max(max_area, min(height[j], height[i]) * (j - i))

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area
