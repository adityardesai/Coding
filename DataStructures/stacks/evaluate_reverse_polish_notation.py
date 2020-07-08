# https://leetcode.com/problems/evaluate-reverse-polish-notation
# TC:O(N)
# SC:O(N)
class Solution:
    def operate(self, a, b, operator):
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            return a / b
        else:
            print('invalid input')

    def evalRPN(self, tokens: List[str]) -> int:

        if not tokens or len(tokens) == 0:
            return -1

        stack = list()

        for token in tokens:
            if token not in ('+', '-', '*', '/'):
                stack.append(int(token))
            else:
                if stack:
                    b = stack.pop()
                    a = stack.pop()
                    result = self.operate(a, b, token)
                    stack.append(int(result))

        return stack[-1]
