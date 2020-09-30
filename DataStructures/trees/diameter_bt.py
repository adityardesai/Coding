"""
Given a binary tree, you need to compute the length of the diameter of the tree. 
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    answer=0
    
    def depth(self, root):
        if root is None:
            return 0
        left=self.depth(root.left)
        right=self.depth(root.right)
        self.answer = max(self.answer, left+right+1)  # Goes through a node so +1
        return max(left,right)+1
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        self.depth(root)
        return self.answer-1 # Because we added +1 for the path, so we added two times same node, delete that extra one
        
