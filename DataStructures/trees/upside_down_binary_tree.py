"""
Given the root of a binary tree, turn the tree upside down and return the new root.

You can turn a binary tree upside down with the following steps:

The original left child becomes the new root.
The original root becomes the new right child.
The original right child becomes the new left child.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursive(self, root):
        if not root.left:
            return root

        new_root=self.recursive(root.left)
        root.left.right=root
        root.left.left=root.right
        
        root.left=root.right=None
        
        return new_root
        
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        return self.recursive(root)
