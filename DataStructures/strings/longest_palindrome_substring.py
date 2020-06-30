# https://leetcode.com/problems/longest-palindromic-substring/
# TC: O(N^2)
# SC: O(N)


class Solution:
    def expand_from_middle(self, s, left, right):
        if not s or left > right:
            return 0

        while (left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1

        return right - left - 1

    def longestPalindrome(self, s: str) -> str:

        if not s or len(s) <= 1:
            return s

        start = 0
        end = 0

        for i in range(len(s)):
            len1 = self.expand_from_middle(s, i, i)
            len2 = self.expand_from_middle(s, i, i + 1)
            l = max(len1, len2)

            if l > (end - start):
                start = i - (l - 1) // 2
                end = i + l // 2

        return s[start:end + 1]
