# https://leetcode.com/problems/flatten-nested-list-iterator/
# TC:
# Constructor: O(M+N)
# next and hasNext: O(1)
# SC: O(N+D), D is the depth of recursion stack and N is the number of the items in list
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):

        self.mlist = list()
        for l in nestedList:
            if l.isInteger():
                self.mlist.append(l.getInteger())
            else:
                self.helper(l.getList())

    def helper(self, nlist):
        for i in nlist:
            if i.isInteger():
                self.mlist.append(i.getInteger())
            else:
                self.helper(i.getList())

    def next(self) -> int:
        if self.hasNext:
            return self.mlist.pop(0)

    def hasNext(self) -> bool:
        return len(self.mlist) > 0


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
