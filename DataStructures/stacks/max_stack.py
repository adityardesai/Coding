# https://leetcode.com/problems/max-stack/
# TC:O(N)
# SC:O(N)
class MaxStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.max_stack = list()

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append(x)
            self.max_stack.append(x)
        else:
            max_ele = max(x, self.max_stack[-1])
            self.max_stack.append(max_ele)
            self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            self.max_stack.pop()
            return self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def peekMax(self) -> int:
        if self.max_stack:
            return self.max_stack[-1]

    def popMax(self) -> int:
        if self.stack:
            max_ele = self.peekMax()
            aux_stack = list()
            while self.top() != max_ele:
                aux_stack.append(self.pop())
            self.pop()
            while aux_stack:
                self.push(aux_stack.pop())
            return max_ele


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
