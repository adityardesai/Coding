# https://leetcode.com/problems/longest-palindromic-substring/
# TC:O(2^N)
# SC:O(1)

class Solution:
    def expand_around_center(self, s, left, right):
        if not s or left>right:
            return 0
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        
        return right-left-1
    
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        
        start=0
        end=0
        for i in range(len(s)):
            len1=self.expand_around_center(s,i,i)
            len2=self.expand_around_center(s,i,i+1)
            res = max(len1, len2)
            
            if (res>end-start):
                start=i-(res-1)//2
                end=i+res//2
        print(start, end)
        return s[start:end+1]
            
