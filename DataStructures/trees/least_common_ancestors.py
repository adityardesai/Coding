# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree
# TC: O(N)
# SC: O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def helper_recursive(self, node, p, q):

        if not node:
            return None

        if node == p or node == q:
            return node

        left = self.helper_recursive(node.left, p, q)
        right = self.helper_recursive(node.right, p, q)

        if left and right:
            return node

        if left and not right:
            return left

        if right and not left:
            return right

    def helper_iterative(self, root, p, q):
        parent_map = {root: None}
        stack = list()
        stack.append(root)

        while p not in parent_map or q not in parent_map:
            node = stack.pop()
            if node.left:
                parent_map[node.left] = node
                stack.append(node.left)
            if node.right:
                parent_map[node.right] = node
                stack.append(node.right)

        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent_map[p]

        while q not in ancestors:
            q = parent_map[q]

        return q

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':

        if not root or not p or not q:
            return False

        #return self.helper_recursive(root, p, q)
        return self.helper_iterative(root, p, q)
