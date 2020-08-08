# https://leetcode.com/problems/sort-characters-by-frequency
# TC: O(N) + O(mlogn)(heap)
# SC: O(m) m = number of tuples in heap and hash_map m<N
from heapq import *
class Solution:
    def heap_helper(self, s):
        hash_map=dict()
        
        for i in range(len(s)):
            ch=s[i]
            if ch in hash_map:
                x=hash_map[ch]
                new_count=-(abs(x[0])+1)
                new_index=i
                hash_map[ch]=(new_count, new_index)
            else:
                hash_map[ch]=(-1,i)
                
        max_heap=list()
        final_result=list()
        
        for k,v in hash_map.items():
            ch=k
            value=v
            heappush(max_heap, (v))
        
        while max_heap:
            res=heappop(max_heap)
            index=res[1]
            count=-res[0]
            final_result.append(count * s[index])
        
        return ''.join(final_result)
            
        
    def frequencySort(self, s: str) -> str:
        if not s:
            return s
        return self.heap_helper(s)
        