"""
https://leetcode.com/problems/word-break-ii/solution/

Each node in the graph represents a postfix of the input string. In particular, we have some nodes with an empty string, which indicates the end of the input string.
Each edge indicates the reduction from one postfix to another. The label on top of each edge indicates the word that is used to trigger the reduction.

TC: O(N^2 +2^N+W)
SC: O(N^2 +2^N+W)
"""

class Solution:
    def helper_top_down(self, s, word_set, cache):
        if not s:
            return [[]]
        if cache[s]:
            return cache[s]
        for end in range(1, len(s)+1):
            prefix = s[:end]
            if prefix in word_set:
                for postfix in self.helper_top_down(s[end:],word_set,cache):
                    cache[s].append([prefix] + postfix)
        
        return cache[s]
    
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s or not wordDict:
            return []
            
        word_set=set(wordDict)
        cache=defaultdict(list) # key: postfix ; value = list of prefix
        # cache["dogo"]: ["do", "go"]
        self.helper_top_down(s, word_set,cache)
        print(cache)
        return [' '.join(word) for word in cache[s]]
        
