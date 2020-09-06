# https://leetcode.com/problems/reverse-words-in-a-string-iii/
# TC: O(N)
# SC: O(1)
class Solution:
    def reverse(self, s, left, right):
        while left<right:
            s[left], s[right] = s[right], s[left]
            left+=1
            right-=1
            
    def reverseWords(self, s: str) -> str:
        i=0
        n=len(s)-1
        s=list(s)
        while i<n:
            j=i
            while j<=n and s[j]!=' ':
                j+=1
            self.reverse(s,i,j-1)
            i=j+1
        
        return ''.join(s)
            
        
