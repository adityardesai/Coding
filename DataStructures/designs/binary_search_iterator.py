# https://leetcode.com/problems/binary-search-tree-iterator/
# TC:O(N)
# SC:O(h)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: TreeNode):

        self.stack = list()
        self.traverse_left(root)

    def traverse_left(self, root):
        if not root:
            return
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        top_most = self.stack.pop()

        if top_most.right:
            self.traverse_left(top_most.right)
        return top_most.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
