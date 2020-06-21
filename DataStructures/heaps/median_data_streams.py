# https://leetcode.com/problems/find-median-from-data-stream/

from heapq import *


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.bigger_bucket = list()  # min heap
        self.smaller_bucket = list()  # max heap

    def rebalance(self, bigger_bucket, smaller_bucket):

        if len(bigger_bucket) - len(smaller_bucket) >= 2:
            heappush(smaller_bucket, -1 * heappop(bigger_bucket))
        elif len(smaller_bucket) - len(bigger_bucket) >= 2:
            heappush(bigger_bucket, -1 * heappop(smaller_bucket))

    def addNum(self, num: int) -> None:
        if not self.smaller_bucket or num < -1 * self.smaller_bucket[0]:
            heappush(self.smaller_bucket, -1 * num)
        else:
            heappush(self.bigger_bucket, num)

        self.rebalance(self.bigger_bucket, self.smaller_bucket)

    def findMedian(self) -> float:

        if len(self.bigger_bucket) == len(self.smaller_bucket):
            x = -1 * self.smaller_bucket[0]
            y = self.bigger_bucket[0]
            return float(x + y) / 2

        if len(self.smaller_bucket) > len(self.bigger_bucket):
            return -1 * self.smaller_bucket[0]
        else:
            return self.bigger_bucket[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
