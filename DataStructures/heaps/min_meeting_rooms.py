# https://leetcode.com/problems/meeting-rooms-ii/
# TC: O(NlogN)
# SC: O(N)
from heapq import *

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        if not intervals:
            return 0
        
        free_room_min_heap = list()
        
        intervals.sort(key=lambda x:x[0])
        
        heappush(free_room_min_heap, intervals[0][1])
        
        print (free_room_min_heap)
        for other_meeting in intervals[1:]:
            
            if free_room_min_heap[0] <= other_meeting[0]:
                heappop(free_room_min_heap)
            
            heappush(free_room_min_heap, other_meeting[1])
        
        print (free_room_min_heap)
        return len(free_room_min_heap)