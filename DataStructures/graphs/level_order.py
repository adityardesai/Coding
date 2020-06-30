# https://leetcode.com/problems/binary-tree-level-order-traversal/
# TC: O(N)
# SC: O(N)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        from collections import deque

        queue = deque()
        result = list()

        queue.append(root)

        while queue:
            temp_list = list()
            level = len(queue)
            for i in range(level):
                node = queue.popleft()
                temp_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(temp_list)

        return result
