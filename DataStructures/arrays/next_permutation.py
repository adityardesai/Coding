"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place and use only constant extra memory.


Find a number that is decreasing from left side
Next find a number that is greater than this number and swap
Reverse the remainig. 

TC:O(N)
SC:O(1)
"""

class Solution:
    def reverse(self,nums, left, right):
        while left<right:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right-=1

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        
        n=len(nums)
        i=n-1
        j=n-1
        
        while (i>0 and nums[i-1]>=nums[i]):
            i=i-1
        
        i=i-1
        
        if i<0:
            self.reverse(nums,0,n-1)
            return
        
        while (j>0 and nums[j]<=nums[i]):
            j=j-1
        
        nums[i],nums[j] = nums[j], nums[i]
        
        self.reverse(nums,i+1,n-1)
        
        
