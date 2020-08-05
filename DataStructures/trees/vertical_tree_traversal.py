# https://leetcode.com/problems/binary-tree-vertical-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def bfs_helper_with_sorting(self, root):
        """
        # TC: O(N) + O(NlogN) ~ O(NlogN)
        # SC: O(N)
        """
        hash_map = dict()
        queue = deque()

        queue.append([root, 0])

        while queue:
            (node, column) = queue.popleft()

            if node:
                if column in hash_map:
                    hash_map[column].append(node.val)
                else:
                    hash_map[column] = [node.val]
                queue.append([node.left, column - 1])
                queue.append([node.right, column + 1])

        keys = sorted(hash_map.keys())

        result = list()

        for key in keys:
            result.append(hash_map[key])

        return result

    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None

        return self.bfs_helper_with_sorting(root)
