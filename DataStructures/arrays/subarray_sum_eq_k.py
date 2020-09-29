# https://leetcode.com/articles/subarray-sum-equals-k/
# TC:O(N)
# SC:O(N)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_map = dict()
        c_sum = 0
        count = 0

        hash_map[0] = 1
        for num in nums:
            c_sum = num + c_sum
            if hash_map.get(c_sum - k):
                count += hash_map.get(c_sum - k)
            hash_map[c_sum] = hash_map.get(c_sum, 0) + 1

        print(hash_map)
        return count
================================================================

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return -1
        hash_map=dict()
        cummulative=0
        count=0
        hash_map[0]=1
        
        for i in range(len(nums)):
            num=nums[i]
            cummulative+=num
            
            if hash_map.get(cummulative-k, 0):
                count+=hash_map[cummulative-k]
            
            hash_map[cummulative] = hash_map.get(cummulative,0) + 1
        
        return count
