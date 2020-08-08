# https://leetcode.com/problems/verifying-an-alien-dictionary/
# TC: O(order)
# SC: O(1)
class Solution:
    
    def custom_comparator(self, word1, word2, char_array):
        char_value=0
        i=0
        j=0
        
        while i<len(word1) and j<len(word2) and char_value==0:
            
            char_value = char_array[ord(word1[i]) - ord('a')] - char_array[ord(word2[j]) - ord('a')] 
            i+=1
            j+=1
        
        if char_value == 0:
            return len(word1) - len(word2)
        else:
            return char_value
            
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if not words or not order:
            return True
        
        char_array=[0] * 26
        
        for i in range(len(order)):
            char_array[ord(order[i]) - ord('a')]=i
        
        for i in range(1, len(words)):
            if (self.custom_comparator(words[i-1], words[i], char_array)) > 0:
                return False
        
        return True
        
        
        