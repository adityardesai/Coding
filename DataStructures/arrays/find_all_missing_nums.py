"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

TC:O(N)
SC:O(1) Output list is not considered

https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        if not nums:
            return []
        
        for i in range(len(nums)):
            correct_index=abs(nums[i])-1
            
            if correct_index>len(nums): continue
                
            if nums[correct_index]>0:
                nums[correct_index]=-1*nums[correct_index]
        
        result=list()
        for i in range(len(nums)):
            if nums[i]>0:
                result.append(i+1)
        
        return result
        
