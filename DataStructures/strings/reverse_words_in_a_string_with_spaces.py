"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

TC:O(N)
SC:O(N)

"""

class Solution:
    def trim_spaces(self, s: str) -> list:
        left, right = 0, len(s) - 1
        # remove leading spaces
        while left <= right and s[left] == ' ':
            left += 1
        
        # remove trailing spaces
        while left <= right and s[right] == ' ':
            right -= 1
        
        # reduce multiple spaces to single one
        output = []
        while left <= right:
            if s[left] != ' ':
                output.append(s[left])
            elif output[-1] != ' ':
                output.append(s[left])
            left += 1
        
        return output
    def reverese(self, s, start, end):
        while start<end:
            s[start],s[end]=s[end],s[start]
            start+=1
            end-=1
    
    def reverse_each_word(self, slist):
        N=len(slist)
        
        start=end=0
        while start<N:
            while end<N and slist[end]!=' ':
                end+=1
            self.reverese(slist,start,end-1)
            start=end+1
            end+=1
    def reverseWords(self, s: str) -> str:
        
        slist=self.trim_spaces(s)
        slist=list(slist)
        self.reverese(slist,0,len(slist)-1)
        
        self.reverse_each_word(slist)
        
        x=''.join(slist)
        return x
