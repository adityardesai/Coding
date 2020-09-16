"""
from collections import deque

Basic Version

class HitCounter:

    def __init__(self):
        self.q=deque()
    

    def hit(self, timestamp: int) -> None:
        self.q.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        while self.q and timestamp - self.q[0]>=300:
            self.q.popleft()
        return len(self.q)
        
"""
class HitCounter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue=[[0,i+1] for i in range(300)]

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        idx = int((timestamp - 1)%300)
        if self.queue[idx][1] == timestamp:
            self.queue[idx][0] += 1
        else:
            self.queue[idx][0] = 1            
            self.queue[idx][1] = timestamp   

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        cnt = 0
        for x in self.queue:
            c,t = x[0],x[1]
            if timestamp - t < 300:
                cnt += c
        return cnt

        
        
        
# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
