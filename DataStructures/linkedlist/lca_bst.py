# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# TC:O(N)
# SC:O(1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lca_recursive_helper(self, root, p, q):
        if not root:
            return None
        if p.val > root.val and q.val > root.val:
            return self.lca_recursive_helper(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lca_recursive_helper(root.left, p, q)
        else:
            return root

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        return self.lca_recursive_helper(root, p, q)
