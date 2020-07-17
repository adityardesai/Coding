# https://leetcode.com/problems/letter-combinations-of-a-phone-number
# TC:O(3^N×4^M)
# SC:O(3^N×4^M)
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

    def recursive_helper2(self, digits, index, temp_list, result):

        if len(temp_list) == len(digits):
            result.append(list(temp_list))
            return
        else:
            for i in range(index, len(digits)):
                for ch in digits[i]:
                    temp_list.append(ch)
                    self.recursive_helper2(digits, i, temp_list, result)
                    temp_list.pop()

    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return ""

        result = list()
        self.recursive_helper(digits, "", result)
        #self.recursive_helper2(digits, 0,[], result)
        return result
