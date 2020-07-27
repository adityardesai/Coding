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
