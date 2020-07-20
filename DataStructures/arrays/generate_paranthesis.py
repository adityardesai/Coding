# https://leetcode.com/problems/generate-parentheses/
# TC: O(2^2n^n)
# SC: O(2^2n^n)
class Solution:
    def backtrack(self, result, max, current_str, open, close):
        if len(current_str) == 2 * max:
            result.append(current_str)
            return

        if open < max:
            self.backtrack(result, max, current_str + '(', open + 1, close)
        if close < open:
            self.backtrack(result, max, current_str + ')', open, close + 1)

    def generateParenthesis(self, n: int) -> List[str]:

        result = list()
        self.backtrack(result, max=n, current_str='', open=0, close=0)
        return result
