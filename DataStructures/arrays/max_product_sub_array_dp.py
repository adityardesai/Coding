"""
"""
class Solution:
    def brute_force(self, nums):
        """
        TC:O(N^2)
        SC:O(1)
        """
        if not nums:
            return 0
        
        result=nums[0]
        for i in range(len(nums)):
            temp=1
            for j in range(i, len(nums)):
                temp=temp*nums[j]
                result=max(result, temp)
        return result
    def dynamic_helper(self, nums):
    """
    TC:O(N)
    SC:O(1)
    """
        if not nums:
            return 0
        
        max_so_far=nums[0]
        min_so_far=nums[0]
        result=max_so_far
        
        for i in range(1, len(nums)):
            num=nums[i]
            temp_max=max(num, max_so_far*num, min_so_far*num)
            min_so_far=min(num, max_so_far*num, min_so_far*num)
            max_so_far=temp_max
            
            result=max(max_so_far, result)
        
        return result
    
    def maxProduct(self, nums: List[int]) -> int:
        #return self.brute_force(nums)
        return self.dynamic_helper(nums)
