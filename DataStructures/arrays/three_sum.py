# https://leetcode.com/problems/3sum/
# TC:O(N^2) + O(NlogN) for sort
# SC:O(N) and also O(NlogN) for sort
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []

        if not nums:
            return result

        nums.sort()

        left = 0
        length = len(nums)
        right = length - 1
        smallest_abs_difference = float('inf')

        for i in range(length - 2):

            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                left = i + 1
                right = length - 1

            while left < right:
                temp_sum = nums[i] + nums[left] + nums[right]
                if temp_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while (left < right and nums[left] == nums[left + 1]):
                        left += 1
                    while (left < right and nums[right] == nums[right - 1]):
                        right -= 1
                    left += 1
                    right -= 1
                elif temp_sum < 0:
                    left += 1
                else:
                    right -= 1

        return result
