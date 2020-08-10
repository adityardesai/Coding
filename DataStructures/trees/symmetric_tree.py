# https://leetcode.com/problems/symmetric-tree/
# TC: O(N)
# SC: O(N)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, t1, t2):

        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False

        return (t1.val == t2.val and (self.helper(t1.right, t2.left)
                                      and self.helper(t1.left, t2.right)))

    def recursive_sol(self, root):
        if not root:
            return True
        return self.helper(root.left, root.right)

    def iterative_sol(self, root):
        if not root:
            return True

        from collections import deque

        queue = deque()
        queue.append(root)
        queue.append(root)

        while queue:
            t1 = queue.popleft()
            t2 = queue.popleft()

            if (t1 is None and t2 is None):
                continue
            if (t1 is None or t2 is None):
                return False

            if t1.val != t2.val:
                return False

            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)

        return True

    def isSymmetric(self, root: TreeNode) -> bool:
        #return self.recursive_sol(root)
        return self.iterative_sol(root)
