# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string
#TC:O(N)
#SC:O(N-D)D=duplicates

class Solution:
    def stack_helper(self, S):
        stack=list()
        
        for i in range(len(S)):
            ch=S[i]
            if not stack:
                stack.append(ch)
            else:
                if ch==stack[-1]:
                    stack.pop()
                else:
                    stack.append(ch)
        
        return ''.join(stack)
    def removeDuplicates(self, S: str) -> str:
        
        if not S:
            return S
        
        return self.stack_helper(S)
        
