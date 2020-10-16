class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_index=0
        non_zero_index=0
        n=len(nums)
        
        while non_zero_index<n:
            if nums[non_zero_index]!=0:
                nums[zero_index], nums[non_zero_index] = nums[non_zero_index],nums[zero_index] 
                zero_index+=1
            non_zero_index+=1
