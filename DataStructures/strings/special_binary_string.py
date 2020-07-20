# https://leetcode.com/problems/special-binary-string/
# TC: O(N^2)
# SC: O(N^2)


class Solution:
    def recursive_helper(self, S):
        balance = 0
        left = 0
        right = 0
        result = list()

        for right in range(len(S)):
            if S[right] == '1':
                balance += 1
            else:
                balance -= 1

            if balance == 0:
                result.append('1' +
                              str(self.recursive_helper(S[left + 1:right])) +
                              '0')
                left = right + 1

        result.sort(reverse=True)
        return ''.join(result)

    def makeLargestSpecial(self, S: str) -> str:

        if not S:
            return ''

        return self.recursive_helper(S)
