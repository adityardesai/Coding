# https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/
# TC: O(N)
# SC: O(N)

import collections
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        if not s:
            return 0
        hash_map=dict()
        for i in range(len(s) - minSize + 1):
            word = s[i:i+minSize]
            if word in hash_map:
                hash_map[word]+=1
            else:
                uniq_count = collections.Counter(word)
                if len(uniq_count)<=maxLetters:
                    hash_map[word]=1
        
        if len(hash_map):
            return max(hash_map.values())
        else:
            return 0
