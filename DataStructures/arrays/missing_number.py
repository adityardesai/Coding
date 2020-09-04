# https://leetcode.com/problems/missing-number/solution/
# TC:O(N)
# SC:O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        N=len(nums)
        
        sum=0
        for i in range(N):
            sum+=nums[i]
        
        expected=(N*(N+1))//2
        
        return expected-sum
        