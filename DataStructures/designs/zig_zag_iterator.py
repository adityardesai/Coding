# https://leetcode.com/problems/zigzag-iterator/
# TC:O(1)
# SC:O(1)

from collections import deque


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = deque(v1)
        self.v2 = deque(v2)
        self.flag = True

    def next(self) -> int:
        r = None
        if self.v1:
            r = self.v1.popleft()
            if self.v2:
                self.v2, self.v1 = self.v1, self.v2
        else:
            r = self.v2.popleft()
        return r

    def hasNext(self) -> bool:
        return len(self.v1) + len(self.v2) > 0


# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
