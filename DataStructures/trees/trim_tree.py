# https://leetcode.com/problems/trim-a-binary-search-tree
# TC: O(N)
# SC: O(N)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node, L, R):

        if not node:
            return None

        elif node.val > R:
            return self.helper(node.left, L, R)
        elif node.val < L:
            return self.helper(node.right, L, R)
        else:
            node.left = self.helper(node.left, L, R)
            node.right = self.helper(node.right, L, R)
            return node

    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:

        if not root:
            return root

        return self.helper(root, L, R)
