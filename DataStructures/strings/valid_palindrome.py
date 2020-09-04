class Solution:
    def is_palindrome(self, input):
        l=len(input)
        mid = l //2
        i=0
        j=len(input)-1
        while i<mid:
            if input[i]!=input[j]:
                return False
            else:
                i+=1
                j-=1
        return True
    def is_palindrom_constant_space(self, s):
        """
        TC:O(n)
        SC:O(1)
        """
        i=0
        j=len(s)-1
        
        while i<j:
            while i<j and not s[i].isalnum():
                i=i+1
            while i<j and not s[j].isalnum():
                j=j-1
            
            if i<j and s[i].lower() != s[j].lower():
                return False
            
            i=i+1
            j=j-1
        
        return True
    def isPalindrome(self, s: str) -> bool:
        
        if not s:
            return True
        s=s.lower()
        
        input = ''
        
        for ch in range(len(s)):
            if s[ch].isalnum():
                input=input+s[ch]
        #return self.is_palindrome(input)
        return self.is_palindrom_constant_space(s)
                
        