class StackEmpty(Exception):
    pass


class Stack:
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, value):
        self._data.append(value)

    def pop(self):
        if self.is_empty():
            raise StackEmpty('Stack is Empty')
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            raise StackEmpty('Stack is Empty')
        top = self._data[-1]
        return top


def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(" length of stack " + str(len(stack)))
    print(stack.pop())
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())


if __name__ == '__main__':
    main()
