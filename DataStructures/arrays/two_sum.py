# https://leetcode.com/problems/two-sum/
# TC:O(N)
# SC:O(N)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        if len(nums) <= 1:
            return []

        hash_map = dict()

        for i in range(len(nums)):

            if target - nums[i] in hash_map and target - nums[i] != nums[i]:
                return [i, hash_map[target - nums[i]]]
            else:
                hash_map[nums[i]] = i

        return [-1, -1]
