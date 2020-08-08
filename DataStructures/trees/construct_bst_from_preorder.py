# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
# TC: O(N)
# SC: O(N)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pre_index=0
        self.preorder=list()
    def helper(self, left, right):
        if self.pre_index == len(self.preorder):
            return None
        value = self.preorder[self.pre_index]
        
        if value<left or value>right:
            return None
        
        root = TreeNode(value)
        self.pre_index+=1
        root.left = self.helper(left=left, right=value)
        root.right = self.helper(left=value, right=right)
        
        return root
        
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder or len(preorder)==0:
            return None
        
        self.pre_index=0
        self.preorder=preorder
        return self.helper(float('-inf'), float('inf'))