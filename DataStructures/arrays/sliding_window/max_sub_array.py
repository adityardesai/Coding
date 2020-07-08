# https://leetcode.com/problems/maximum-subarray/
# TC:O(N)
# SC:O(1)
class Solution:
    def get_max_sub_array_sum(self, nums):
        from collections import deque

        wstart = 0
        result_max = float('-inf')
        temp_max = 0
        result_arr = deque()

        for i in range(len(nums)):
            temp_max += nums[i]
            result_max = max(result_max, temp_max)
            while temp_max < 0:
                temp_max -= nums[wstart]
                wstart += 1
        return result_max

    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        return self.get_max_sub_array_sum(nums)
