# https://leetcode.com/problems/palindrome-permutation/
# TC: O(N)
# SC: O(1)
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:

        if not s or len(s) == 0:
            return True

        arr = [0] * 128
        count = 0

        for i in range(len(s)):
            ch = s[i]
            ascii_value = ord(ch)
            arr[ascii_value] += 1

        for i in range(len(arr)):
            count = count + (arr[i] % 2)

        return count <= 1
