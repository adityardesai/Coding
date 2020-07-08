# https://leetcode.com/problems/valid-anagram/
# TC: O(N)
# SC: O(1)
class Solution:
    def anagram_helper(self, s, t):
        char_array = [0] * 26

        for i in range(len(s)):
            char_array[ord(s[i]) - ord('a')] += 1
            char_array[ord(t[i]) - ord('a')] -= 1

        for ch in char_array:
            if ch != 0:
                return False

        return True

    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        return self.anagram_helper(s, t)
