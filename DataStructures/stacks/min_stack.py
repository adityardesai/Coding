#https://leetcode.com/problems/min-stack/
#TC:O(1)
#SC:O(N)


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x, x))
        else:
            item_on_top = self.stack[-1]
            min_to_push = min(x, item_on_top[1])
            self.stack.append((x, min_to_push))

    def pop(self) -> None:
        if self.stack:
            return self.stack.pop()[1]

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
