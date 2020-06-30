#https://leetcode.com/problems/longest-substring-without-repeating-characters/
# TC: O(N)
# SC: O(N)


class Solution:
    def hash_set_sliding_window(self, s):
        n = len(s)
        hash_set = set()
        left = 0
        right = 0
        ans = 0

        while right < n:
            if s[right] not in hash_set:
                hash_set.add(s[right])
                ans = max(ans, len(hash_set))
                right += 1
            else:
                hash_set.remove(s[left])
                left += 1
        return ans

    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0
        return self.hash_set_sliding_window(s)
