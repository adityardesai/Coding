# https://leetcode.com/problems/next-permutation/
# TC: O(N)
# SC: O(1)
class Solution:
    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1
            left += 1

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 0:
            return nums

        n = len(nums)
        i = n - 1

        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1

        if i == 0:
            self.reverse(nums, 0, n - 1)
            return

        k = i - 1
        j = n - 1

        while nums[j] <= nums[k]:
            j -= 1

        nums[k], nums[j] = nums[j], nums[k]

        left = k + 1
        right = n - 1
        self.reverse(nums, left, right)
