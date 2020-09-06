# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# TC: O(3^N×4^M)
# SC: O(3^N×4^M)

class Solution:
    phone_map = {
                 '2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']
            }
    def backtrack_helper(self, digits, result, temp_list, start):
        if start==len(digits):
            temp_list=''.join(temp_list)
            result.append(str(temp_list))
            return
        else:
            tmp=self.phone_map.get(digits[start])
            for i in range(len(tmp)):
                temp_list.append(tmp[i])
                self.backtrack_helper(digits, result, temp_list,start+1)
                temp_list.pop()
                      
    def letterCombinations(self, digits: str) -> List[str]:
        
        
        if not digits:
            return []
        
        result=list()
        temp_list=list()
        
        self.backtrack_helper(digits,result,temp_list,0)
        
        return result
        
        
