# https://leetcode.com/problems/shuffle-the-array/
# TC:O(N)
# SC:O(1)


class Solution:
    def brute_force_extra_space(self, nums, n):
        mid=n
        i=0
        j=mid
        result=list()
        
        while i<mid and j<2*n:
            result.append(nums[i])
            result.append(nums[j])
            i+=1
            j+=1
        
        return result
    
    def constant_space(self, nums, n):
        
        i=n-1
        j=2*n - 1
        
        while j>=n:
            nums[j]=nums[j]<<10
            nums[j]=nums[i] | nums[j]
            i=i-1
            j=j-1
        
        j=n
        i=0
        
        while j<2*n:
            nums[i] = nums[j]&1023
            nums[i+1] = nums[j]>>10
            j+=1
            i+=2
        
        return nums
        
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        if not nums:
            return nums
        #return self.brute_force_extra_space(nums, n)
        return self.constant_space(nums, n)
        
            
