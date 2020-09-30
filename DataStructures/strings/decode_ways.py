"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

Example 1:

Input: s = "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

TC:O(N)
SC:O(N)

Consider one digit at a time and then two digit at a time

"""

class Solution:
    def helper(self,s,cache,start_index):
        
        if start_index==len(s):
            return 1
        
        if s[start_index]=='0':
            return 0
        
        if start_index==len(s)-1:
            return 1
        
        if cache.get(start_index):
            return cache[start_index]
        
        ans=self.helper(s, cache, start_index+1)
        
        if (int(s[start_index:start_index+2])<=26):
            ans=ans+self.helper(s, cache, start_index+2)
        
        cache[start_index]=ans
        
        return ans
        
    def numDecodings(self, s: str) -> int:
        if not s:
            return -1
        
        cache=dict()
        start_index=0
        
        return self.helper(s,cache,start_index)
