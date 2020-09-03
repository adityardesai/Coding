# https://leetcode.com/problems/combination-sum/solution/
# TC:O(N^t/m) t=target and m=minimal_value
# SC:O(t/m)

class Solution:
    def backtrack_helper(self, candidates, target, result, temp_result, start):
        
        if target==0:
            result.append(list(temp_result))
        elif target<0:
            return
        else:
            for i in range(start, len(candidates)):
                c=candidates[i]
                temp_result.append(c)
                self.backtrack_helper(candidates, target-c, result, temp_result,i)
                temp_result.pop()
                
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        if not candidates or not target:
            return []
        
        result=list()
        temp_result=list()
        start_index=0
        
        self.backtrack_helper(candidates, target, result, temp_result,start_index)
        return result
        
