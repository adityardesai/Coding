# https://leetcode.com/problems/longest-common-prefix/
# TC: O(S) S=is the sum of all characters in all strings
# SC: O(1)
class Solution:
    def helper_lca(self, strs):
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix):
                prefix = prefix[0:len(prefix) - 1]
                if not prefix:
                    return ''
        return prefix

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or len(strs) == 0:
            return ''
        return self.helper_lca(strs)
