# https://leetcode.com/problems/decode-string/
# TC: O(N)
# SC: O(N)
class Solution:
    def parse_string(self, s):
        stack_count = list()
        stack_result = list()

        current_str = ''
        current_num = 0

        for ch in s:
            if ch.isdigit():
                current_num = current_num * 10 + int(ch)
            elif ch == '[':
                stack_count.append(current_num)
                stack_result.append(current_str)
                current_str = ''
                current_num = 0
            elif ch == ']':
                count = stack_count.pop()
                new_str = count * current_str
                current_str = stack_result.pop()
                current_str = current_str + new_str
            else:
                current_str = current_str + ch

        return current_str

    def decodeString(self, s: str) -> str:
        if not s:
            return ''
        return self.parse_string(s)
