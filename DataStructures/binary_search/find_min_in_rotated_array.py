"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1

TC:O(LogN)
SC:O(1)
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if not nums:
            return -1
        
        L = len(nums)
        low = 0
        high = L-1
        
        while low<high:
            
            mid = (low+high)//2
            
            if nums[mid] > nums[high]:
                low=mid+1
            else:
                high=mid
        
        return nums[low]
