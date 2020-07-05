# https://leetcode.com/problems/valid-parentheses
# TC: O(N)
# SC: O(N)
class Solution:
    def isValid(self, s: str) -> bool:

        if not s:
            return True

        stack = list()

        for ch in s:
            if ch in ('(', '[', '{'):
                stack.append(ch)
            elif ch == ')' and len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            elif ch == ']' and len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            elif ch == '}' and len(stack) > 0 and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(ch)

        return len(stack) == 0
