"""
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1

TC:O(N)
SC:O(1)
"""




class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        first_word_index=float('inf')
        second_word_index=float('inf')
        min_distance=float('inf')
        
        for i in range(len(words)):
            word = words[i]
            if word == word1:
                first_word_index = i
            elif word == word2:
                second_word_index = i
            
            min_distance = min(min_distance, abs(first_word_index - second_word_index))
        
        return min_distance
