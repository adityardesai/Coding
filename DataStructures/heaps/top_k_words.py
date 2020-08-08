# https://leetcode.com/problems/top-k-frequent-words/
# TC: O(N+klogN)
# SC: O(N)
from heapq import *

class Solution:
    def heap_helper(self, words, k):
        hash_map=dict()
        
        for i in range(len(words)):
            word=words[i]
            if word in hash_map:
                x=hash_map[word]
                new_count=-(abs(x[0])+1)
                hash_map[word]=(new_count,word)
            else:
                hash_map[word]=(-1,word)
        
        # This will improve efficiency
        max_heap=list()
        max_heap=list(hash_map.values())
        heapify(max_heap)
        
        #for key,v in hash_map.items():
        #    heappush(max_heap, v)
        
        final_result=list()
        
        while k:
            res=heappop(max_heap)
            final_result.append(res[1])
            k-=1
        
        return final_result
        
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if not words or not k:
            return []
        return self.heap_helper(words, k)
        