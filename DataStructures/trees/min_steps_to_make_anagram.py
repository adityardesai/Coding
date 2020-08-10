# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
# TC: O(N)
# SC: O(M) M<=N
class Solution:
    def minSteps(self, s: str, t: str) -> int:

        d = dict()

        for ch in s:
            d[ch] = d.get(ch, 0) + 1

        count = 0

        for ch in t:
            if ch in d and d[ch] > 0:
                d[ch] = d[ch] - 1
            else:
                print(ch)
                count += 1

        return count
