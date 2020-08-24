# https://leetcode.com/problems/ransom-note/s
# TC:O(m)
# SC:O(1) alphabets are always 26 

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    
        if len(ransomNote) > len(magazine): 
            return False

        mag_hash_map = dict()

        for ch in magazine:
            mag_hash_map[ch] = mag_hash_map.get(ch, 0)+1

        for c in ransomNote:
            if c not in mag_hash_map:
                return False
            if mag_hash_map[c]<=0:
                return False
            mag_hash_map[c]-=1

        return True
        
