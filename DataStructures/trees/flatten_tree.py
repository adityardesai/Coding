# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# TC: O(N)
# SC: O(N)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursive_helper(self, root):
        if not root:
            return None
        
        if not root.left and not root.right:
            return root
    
        left_temp=self.recursive_helper(root.left)
        right_temp=self.recursive_helper(root.right)
        
        if left_temp:
            left_temp.right=root.right
            root.right=root.left
            root.left=None
        
        if right_temp:
            return right_temp
        else:
            return left_temp
        
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        
        return self.recursive_helper(root)