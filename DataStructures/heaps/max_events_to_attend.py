# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/
# TC:O(nlogn) + O(klogn) + O(klogn)
# SC:O(1)

from heapq import *

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        if not events:
            return 
        
        events=sorted(events)
        max_days = max(event[1] for event in events)
        day=1
        count=0
        min_heap=list()
        i=0
        while day<=max_days:
            # min_heap is empty
            if i<len(events) and not min_heap:
                day=events[i][0]
            
            # can attend this event, so push to heap
            while i<len(events) and events[i][0]<=day:
                heappush(min_heap, events[i][1])
                i=i+1
            
            # event already completed, so pop from heap
            while min_heap and min_heap[0]<day:
                heappop(min_heap)
            
            # count how many events we were able to attend so far
            if min_heap:
                heappop(min_heap)
                count+=1    
            elif i>=len(events):
                break
            day+=1
        return count
        
