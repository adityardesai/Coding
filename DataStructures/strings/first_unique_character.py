# https://leetcode.com/problems/first-unique-character-in-a-string/
# TC:O(N)
# SC:O(1)
class Solution:
    def firstUniqChar_another(self, s: str) -> int:
        
        if len(s)==0:
            return -1
        
        arr=[0]*26
        
        for c in range(len(s)):
            asciivalue=ord(s[c])-97
            arr[asciivalue]+=1
        
        for c in range(len(s)):
            asciivalue=ord(s[c])-97
            if arr[asciivalue]==1:
                return c
        return -1
    def firstUniqChar(self, s: str) -> int:
        
        if len(s)==0:
            return -1
        
        h_map = dict()
        
        for ch in s:
            h_map[ch] = h_map.get(ch,0)+1
        
        for i in range(len(s)):
            if h_map[s[i]]==1:
                return i

        return -1