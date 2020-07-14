# https://leetcode.com/problems/contains-duplicate-ii/
# TC:O(N)
# SC:O(N)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = dict()
        result = False

        for i in range(len(nums)):
            num = nums[i]
            if num in hash_map:
                old_index = hash_map[num]
                hash_map[num] = i
                if i - old_index <= k:
                    result = True
            hash_map[num] = i
        return result
