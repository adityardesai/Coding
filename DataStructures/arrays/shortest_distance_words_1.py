"""
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1


"""




class Solution:
    def pre_process_helper(self, words, word1, word2):
        """
        TC:O(N)
        SC:O(N)
        """
        pre_process_map=dict()
        
        for i in range(len(words)):
            if words[i] in pre_process_map:
                pre_process_map[words[i]].append(i)
            else:
                pre_process_map[words[i]]=[i]
        
        loc1=pre_process_map[word1]
        loc2=pre_process_map[word2]
        l1=0
        l2=0
        min_distance = float('inf')
        
        while l1<len(loc1) and l2<len(loc2):
            min_distance=min(min_distance, abs(loc1[l1] - loc2[l2]))
            if loc1[l1] < loc2[l2]:
                l1+=1
            else:
                l2+=1
        
        return min_distance
                
    def one_pass_helper(self, words, word1, word2):
        """
        TC:O(N)
        SC:O(1)
        """
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
    
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        
        #return self.one_pass_helper(words, word1, word2)
        return self.pre_process_helper(words, word1, word2)
