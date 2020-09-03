class Solution:
    def backtrack(self, result, nums, temp, start_index):
        result.append(list(temp))
        for i in range(start_index, len(nums)):
            temp.append(nums[i])
            self.backtrack(result, nums, temp,i+1)
            temp.pop()
            
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        result = list()
        start_index = 0
        self.backtrack(result,nums, list(), start_index)
        return result
        
