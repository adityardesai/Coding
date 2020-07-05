# https://leetcode.com/problems/binary-tree-inorder-traversal/
# TC: O(Height of the tree) or equivalent in terms of Number of nodes is O(N)
# SC: O(N)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursive_inorder(self, root, result):
        if not root:
            return
        self.recursive_inorder(root.left, result)
        result.append(root.val)
        self.recursive_inorder(root.right, result)

    def iterative_inorder(self, root, result):

        if not root:
            return
        stack = list()

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                result.append(root.val)
                root = root.right

    def inorderTraversal(self, root: TreeNode) -> List[int]:

        if not root:
            return root
        result = list()
        #self.recursive_inorder(root,result)
        self.iterative_inorder(root, result)
        return result
