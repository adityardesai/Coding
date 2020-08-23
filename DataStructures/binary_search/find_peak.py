# https://leetcode.com/problems/find-peak-element/
# TC:O(logN)
# SC:O(1)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        
        if nums is None:
            return -1
        
        left=0
        right=len(nums)-1
        
        while left<right:
            mid=(left+right)//2
            
            if nums[mid]<nums[mid+1]:
                left=mid+1
            else:
                right=mid
        
        return left
