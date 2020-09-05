# https://leetcode.com/problems/palindrome-permutation/
# TC:O(N)
# SC:O(N)

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if not s:
            return False
        
        n=len(s)
        hash_map=dict()
        count=0
        
        for ch in s:
            hash_map[ch]=hash_map.get(ch,0)+1
        
        for k,v in hash_map.items():
            count = count + (v%2)
        
        return count<=1
            
            
        
