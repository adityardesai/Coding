# https://leetcode.com/problems/binary-tree-right-side-view/
# TC: O(N) N=Number of nodes
# SC: O(D) D=Tree Diameter
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def helper_level_order(self, root):
        queue = deque()
        queue.append(root)
        result = list()
        while queue:
            level = len(queue)
            for i in range(level):
                node = queue.popleft()
                if i == level - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result

    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        return self.helper_level_order(root)
