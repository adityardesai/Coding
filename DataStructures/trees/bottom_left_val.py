# https://leetcode.com/problems/find-bottom-left-tree-value/
# TC: O(N)
# SC: O(N)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:

        stack = list()
        stack.append((root, 1))
        max_level = 0
        result = 0

        while stack:
            curr, level = stack.pop()
            if curr:
                if level > max_level:
                    max_level = level
                    result = curr.val
                stack.append((curr.right, level + 1))
                stack.append((curr.left, level + 1))
        return result
