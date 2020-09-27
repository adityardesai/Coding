"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1

TC:O(N)
SC:O(1)

https://leetcode.com/problems/first-missing-positive/
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        
        # if 1 not in nums:
        #     return 1
        
        for i in range(n):
            if nums[i]<=0 or nums[i]>n:
                nums[i]=n+1 # (n+1) is a flag
        
        for i in range(n):
            correct_pos = abs(nums[i])
            if correct_pos>n:
                continue
            correct_pos=correct_pos-1
            if nums[correct_pos]>0:
                    nums[correct_pos] = -1 * nums[correct_pos]
        
        for i in range(n):
            if nums[i]>0:
                return i+1
        
        return n+1
        
