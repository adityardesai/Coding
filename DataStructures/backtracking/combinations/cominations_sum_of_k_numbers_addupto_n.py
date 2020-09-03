# https://leetcode.com/problems/combination-sum-iii/solution/
# TC: O(9! / (9-k)!)
# SC: O(K)

class Solution:
    def backtrack_helper(self, k, target, result, temp_list, next_num):
        if len(temp_list)==k and target==0:
            result.append(list(temp_list))
        elif target<0:
            return
        else:
            for i in range(next_num, 9):
                temp_list.append(i+1)
                self.backtrack_helper(k,target-i-1,result, temp_list, i+1)
                temp_list.pop()
        
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if not k or not n:
            return []
        result=list()
        temp_list=list()
        start_num=0
        self.backtrack_helper(k,n,result, temp_list, start_num)
        return result
        
