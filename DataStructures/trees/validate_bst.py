# https://leetcode.com/problems/validate-binary-search-tree/
# TC: O(N)
# SC: O(N)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper_recursive(self, node, lower, higher):

        if not node:
            return True

        value = node.val

        if value <= lower or value >= higher:
            return False

        if not self.helper_recursive(node.right, value, higher):
            return False

        if not self.helper_recursive(node.left, lower, value):
            return False

        return True

    def inorder_iterative(self, root):
        stack = list()
        inorder = float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True

    def iterative_helper(self, root):

        if not root:
            return True

        stack = list()
        stack.append((root, float('-inf'), float('inf')))

        while stack:
            root, lower, higher = stack.pop()
            if not root:
                continue
            value = root.val

            if value <= lower or value >= higher:
                return False
            stack.append((root.right, value, higher))
            stack.append((root.left, lower, value))

        return True

    def isValidBST(self, root: TreeNode) -> bool:

        if not root:
            return True

        lower = float('-inf')
        higher = float('inf')
        #return self.helper_recursive(root, lower, higher)
        #return self.inorder_iterative(root)
        return self.iterative_helper(root)
