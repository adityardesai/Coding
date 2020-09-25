"""

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

TC:O(4^n/sqrt(n))
SC:O(4^n/sqrt(n))

"""




class Solution:
    def backtrack(self, result, open_count, close_count, temp_str,n):
        if len(temp_str)==2*n:
            result.append(temp_str)
            return 
        else:
            if open_count<n:
                self.backtrack(result, open_count+1, close_count, temp_str+'(',n)
            if close_count<open_count:
                self.backtrack(result, open_count, close_count+1, temp_str+')',n)
    def generateParenthesis(self, n: int) -> List[str]:
        if not n:
            return []
        open_count=0
        close_count=0
        result=list()
        temp_str=str()
        self.backtrack(result, open_count, close_count, temp_str,n)
        
        return result
        
        
        
        
