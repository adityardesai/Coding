class Solution:
    def helper_dynamic(self, nums):
        if not nums or len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0], nums[1])
        """
        dp[i] represents the amount of money robbed till i'th house
        """
        dp=[-1] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i]=max(dp[i-2]+nums[i], dp[i-1])
        
        return dp[len(nums)-1]
            
    def rob(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return nums[0]
        
        rob_first = self.helper_dynamic(nums[1:])
        rob_last = self.helper_dynamic(nums[:-1])
        return max(rob_first, rob_last)
        
