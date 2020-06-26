class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        if not v1 and not v2:
            return

        self.arr = []
        self.index = -1
        self.add_to_list(v1, v2)

    def add_to_list(self, v1, v2):

        i = 0
        j = 0

        while i < len(v1) and j < len(v2):
            self.arr.append(v1[i])
            self.arr.append(v2[j])
            i += 1
            j += 1

        while i < len(v1):
            self.arr.append(v1[i])
            i += 1

        while j < len(v2):
            self.arr.append(v2[j])
            j += 1

    def next(self) -> int:
        self.index += 1
        return self.arr[self.index]

    def hasNext(self) -> bool:
        if self.arr:
            return (self.index + 1) < len(self.arr)
        else:
            return -1


# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
