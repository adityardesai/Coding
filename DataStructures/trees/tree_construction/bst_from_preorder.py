"""
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
TC:O(N)
SC:O(N)

"""


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
        
        root.left = self.helper(left, value)
        root.right = self.helper(value, right)
        
        return root
        
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder or len(preorder)==0:
            return None
        
        self.pre_index=0
        self.preorder=preorder
        return self.helper(float('-inf'), float('inf'))
