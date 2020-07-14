# https://leetcode.com/problems/insert-delete-getrandom-o1/
# TC:O(1)
class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = dict()
        self.mlist = list()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.hashmap:
            return False
        self.hashmap[val] = len(self.mlist)  # index
        self.mlist.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.hashmap:
            return False

        last_ele = self.mlist[-1]
        idx_to_swap = self.hashmap[val]

        self.mlist[idx_to_swap] = last_ele
        self.hashmap[last_ele] = idx_to_swap

        self.mlist.pop()
        del self.hashmap[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.mlist)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
