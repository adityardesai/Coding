# https://leetcode.com/problems/alien-dictionary/solution/
# TC: O(C) C-> all length of given words
# SC: O(1) or O(U + min(U^2, N)) 
from collections import deque
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        adj_list_map=dict()
        counts_map=dict()
        
        for word in words:
            for c in word:
                counts_map[c]=0
                adj_list_map[c]=list()
        
        print(adj_list_map)
        print(counts_map)
        
        for i in range(len(words)-1):
            word1=words[i]
            word2=words[i+1]
            
            if len(word1) > len(word2) and word1.startswith(word2):
                return ''
            
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    adj_list_map[word1[j]].append(word2[j])
                    counts_map[word2[j]] = counts_map[word2[j]] + 1
                    break
        
        result=list()
        
        queue=deque()
        
        for c in counts_map:
            if counts_map[c]==0:
                queue.append(c)
        
        print(adj_list_map)
        print(counts_map)
        
        while queue:
            c=queue.popleft()
            result.append(c)
            for n in adj_list_map[c]:
                counts_map[n] = counts_map[n]-1
                if counts_map[n]==0:
                    queue.append(n)
        
        if len(result)<len(counts_map):
            return ''
        return ''.join(result)