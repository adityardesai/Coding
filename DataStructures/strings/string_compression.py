# https://leetcode.com/problems/string-compression/
# TC:O(N)
# SC:O(1)
class Solution:
    def compress(self, chars: List[str]) -> int:
        if chars == None or len(chars) < 1:
            return 0;
        i=0
        index=0
        
        while i< len(chars):
            j=i
            while j< len(chars) and chars[i]==chars[j]:
                j+=1
            chars[index]=chars[i]
            index+=1
            if j-i > 1:
                count=str(j-i)
                for ch in count:
                    chars[index]=ch
                    index+=1
            i=j
        return index