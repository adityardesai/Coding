# https://leetcode.com/problems/combination-sum-ii/
# TC:O(N^T/M)
# SC:O(N^T/M)

class Solution:
    def backtrack_helper(self, candidates, target, result, temp_list, start):
        if target==0:
            result.append(list(temp_list))
        elif target<0:
            return
        else:
            for i in range(start, len(candidates)):
                if i> start and candidates[i]==candidates[i-1]:
                    continue
                n=candidates[i]
                temp_list.append(n)
                self.backtrack_helper(candidates, target-n, result, temp_list, i+1)
                temp_list.pop()
                
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates or not target:
            return []
        result=list()
        temp_list=list()
        start=0
        candidates.sort()
        self.backtrack_helper(candidates, target, result, temp_list,start)
        return result
        
        
        
        
