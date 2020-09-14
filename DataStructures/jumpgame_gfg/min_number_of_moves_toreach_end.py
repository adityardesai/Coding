# https://www.geeksforgeeks.org/minimum-number-of-jumps-to-reach-end-of-a-given-array/

class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        jumps = [float('inf')] * n
        
        jumps[0]=0
        
        for i in range(1,n):
            for j in range(0,i):
                if j+nums[j]>=i:
                    jumps[i]=min(jumps[i], jumps[j]+1)
        
        return jumps[n-1]
