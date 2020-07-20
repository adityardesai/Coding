# https://leetcode.com/problems/product-of-array-except-self/
# TC: O(N)
# SC: O(1) : Result is not considered as extra space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if not nums:
            return nums

        L = len(nums)

        left = [0] * L
        right = [0] * L

        left[0] = 1
        right[L - 1] = 1

        for i in range(1, L):
            left[i] = left[i - 1] * nums[i - 1]

        for j in range(L - 2, -1, -1):
            right[j] = right[j + 1] * nums[j + 1]

        for i in range(L):
            left[i] = left[i] * right[i]

        return left
