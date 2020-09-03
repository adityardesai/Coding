# https://leetcode.com/problems/permutations-ii/
# TC: O(2^N)
# SC: O(2^N)

class Solution:
    def backtrack(self, result, nums, temp_list, used):
        if len(temp_list) == len(nums):
            result.append(list(temp_list))
        else:
            for i in range(len(nums)):
                if (used[i] or (i>0 and nums[i]==nums[i-1] and not used[i-1])):
                    continue
                
                used[i] = True
                temp_list.append(nums[i])
                
                self.backtrack(result,nums,temp_list, used)
                
                used[i] = False
                temp_list.pop()
                
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = list()
        temp_list = list()
        nums.sort()
        self.backtrack(result,nums,temp_list,[False] * len(nums))
        return result
        
