# https://leetcode.com/problems/permutations/
# TC:O(N!) 
# SC:O(N!)


class Solution:
    def backtrack(self, result, nums, temp_list):
        if len(temp_list) == len(nums):
            result.append(list(temp_list))
        else:
            for num in nums:
                if num in temp_list:
                    continue
                temp_list.append(num)
                self.backtrack(result,nums,temp_list)
                temp_list.pop()
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = list()
        temp_list = list()
        self.backtrack(result,nums,temp_list)
        return result
