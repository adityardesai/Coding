class Solution:
    def romanToInt(self, s: str) -> int:
        
        sum = 0
        
        roman_map = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        start = 0
        end = len(s)
        
        while(start<end):
            if start+1<end and (roman_map[s[start+1]]>roman_map[s[start]]):
                sum = sum + (roman_map[s[start+1]] - roman_map[s[start]])
                start += 2
            else:
                sum = sum + roman_map[s[start]]
                start += 1
        return sum