# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# TC: O(3^N * 4^M) where N is the number of digits in the input that maps to
# 3 letters (e.g. 2, 3, 4, 5, 6, 8) and M is the number of digits in the input that maps
# to 4 letters (e.g. 7, 9), and N+M is the total number digits in the input.
# SC: O(3^N * 4^M)
phone_map = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}


class Solution:
    def recursive_helper(self, digits, temp_result, result):

        if len(digits) == 0:
            result.append(temp_result)
            return
        else:
            for letter in phone_map[digits[0]]:
                self.recursive_helper(digits[1:], temp_result + letter, result)

    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return ""

        result = list()
        self.recursive_helper(digits, "", result)
        #self.recursive_helper2(digits, 0,[], result)
        return result
