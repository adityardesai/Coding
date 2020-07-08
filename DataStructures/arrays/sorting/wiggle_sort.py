# https://leetcode.com/problems/wiggle-sort/
# This is without duplicates
# TC: O(NlogN) or O(N)
# SC: O(1)
class Solution:
    def helper_sort(self, nums):
        """
        TC:O(NlogN)
        SC:O(1)
        """
        nums.sort()
        i = 0
        for i in range(1, len(nums) - 1, i + 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        return nums

    def helper_in_place(self, nums):
        """
        TC:O(N)
        SC:O(1)
        """
        flag = True
        for i in range(0, len(nums) - 1):
            if flag:
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            else:
                if nums[i] < nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            flag != flag

    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums

        return self.helper_sort(nums)
