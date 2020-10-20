"""
Given a string s and a string t, check if s is subsequence of t.
A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) 
of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).
Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?
Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

https://leetcode.com/problems/is-subsequence/

TC:O(|T|)
SC:O(1)

"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if s and not t:
            return False
        
        i=0
        j=0
        
        while i<len(s) and j<len(t):
            
            if s[i] == t[j]:
                i+=1
            j+=1
        
        return i == len(s)
