# https://leetcode.com/problems/isomorphic-strings/
# O(N)
# O(N)

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if not s or not t:
            return True
        
        s_map=dict()
        t_map=dict()
        
        
        for i in range(len(s)):
            if s[i] not in s_map:
                if t[i] not in s_map.values():
                    s_map[s[i]]=t[i]
                else:
                    return False
            elif s_map[s[i]] != t[i]:
                return False
        
        return True
