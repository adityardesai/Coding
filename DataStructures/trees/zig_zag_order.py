# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# TC: O(N)
# SC: O(N)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        from collections import deque

        queue = deque()
        result = list()
        right_to_left = True

        queue.append(root)

        while queue:
            temp_list = deque()
            level = len(queue)
            for i in range(level):
                node = queue.popleft()
                if right_to_left:
                    temp_list.append(node.val)
                else:
                    temp_list.appendleft(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(temp_list)
            right_to_left = not right_to_left

        return result
