"""

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

TC: O(N)
SC: O(N)

"""



class Solution:
    def isValid(self, s: str) -> bool:
        
        if not s:
            return True
        
        stack=list()
        
        for ch in s:
            if ch in ('(', '[', '{'):
                stack.append(ch)
            elif ch == ')' and len(stack)>0 and stack[-1]=='(':
                stack.pop()
            elif ch == ']' and len(stack)>0 and stack[-1]=='[':
                stack.pop()
            elif ch == '}' and len(stack)>0 and stack[-1]=='{':
                stack.pop()
            else:
                stack.append(ch)
        
        return len(stack)==0
