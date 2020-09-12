# https://leetcode.com/problems/closest-binary-search-tree-value
# TC: O(H)
# SC: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        if not root:
            return root.val
        
        abs_diff=float('inf')
        result=None
        curr=root
        
        while curr:
            if abs_diff > abs(curr.val - target):
                abs_diff = abs(curr.val - target)
                result = curr.val
            if curr.val>target:
                curr=curr.left 
            else:
                curr=curr.right
        return result
