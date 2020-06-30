# https://leetcode.com/problems/trapping-rain-water/
# TC: O(N)
# SC: O(2N)
class Solution:
    def find_left_max(self, height, left_arr, n):
        for i in range(1, n):
            left_arr[i] = max(left_arr[i - 1], height[i])

    def find_right_max(self, height, right_arr, n):
        for i in range(n - 2, 0, -1):
            right_arr[i] = max(right_arr[i + 1], height[i])

    def trap(self, height: List[int]) -> int:
        """
        [0,1,0,2,1,0,1,3,2,1,2,1]
        """
        if not height:
            return 0

        n = len(height)
        left_arr = [0] * n
        left_arr[0] = height[0]
        right_arr = [0] * n
        right_arr[n - 1] = height[n - 1]
        result = 0

        self.find_left_max(height, left_arr, n)
        self.find_right_max(height, right_arr, n)

        for i in range(1, n - 1):
            result = result + (min(left_arr[i], right_arr[i]) - height[i])

        return result
